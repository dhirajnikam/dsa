"""Regression checks for safe feedback, persistence, navigation, and recall scheduling."""
import ast
from datetime import date
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import learn


class LearningTests(unittest.TestCase):
    def test_first_task_and_progression(self):
        state = {}
        kind, first = learn.today_task(state, today=date(2026, 1, 1))
        self.assertEqual(first, learn.resolve('00/01'))
        learn.record_pass(state, first.relative_to(learn.ROOT).as_posix(), date(2026, 1, 1))
        self.assertEqual(learn.today_task(state, today=date(2026, 1, 1))[1], learn.resolve('00/02'))
        self.assertEqual(learn.today_task(state, today=date(2026, 1, 2)), ('Recall review', first))

    def test_repeated_pass_does_not_postpone_review(self):
        state = {}
        learn.record_pass(state, 'task', date(2026, 1, 1))
        learn.record_pass(state, 'task', date(2026, 1, 8))
        self.assertEqual(state['task']['due'], '2026-01-02')

    def test_review_intervals_and_same_day_guard(self):
        state = {}
        learn.record_pass(state, 'task', date(2026, 1, 1))
        learn.record_review(state, 'task', date(2026, 1, 2))
        self.assertEqual(state['task']['due'], '2026-01-05')
        with self.assertRaises(ValueError):
            learn.record_review(state, 'task', date(2026, 1, 2))
        learn.record_review(state, 'task', date(2026, 1, 5))
        self.assertEqual(state['task']['due'], '2026-01-12')
        learn.record_review(state, 'task', date(2026, 1, 12))
        self.assertEqual(state['task']['due'], '2026-01-26')
        learn.record_review(state, 'task', date(2026, 1, 26))
        self.assertEqual(state['task']['due'], '2026-02-09')

    def test_cannot_review_unpassed_task(self):
        with self.assertRaises(ValueError):
            learn.record_review({}, 'task')

    def test_stale_removed_task_does_not_block_queue(self):
        state = {'no-longer-present.py': {'due': '2000-01-01', 'reviews': 0}}
        self.assertEqual(learn.today_task(state)[1], learn.resolve('00/01'))

    def test_complete_first_lap_has_a_clear_end(self):
        state = {learn.resolve(s).relative_to(learn.ROOT).as_posix(): {'due': '2099-01-01', 'reviews': 0}
                 for s in learn.CORE}
        self.assertEqual(learn.today_task(state, today=date(2026, 1, 1)), (None, None))

    def test_state_round_trip_and_corruption_preserved(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'state.json'
            self.assertEqual(learn.read_state(path), {})
            state = {'task': {'due': '2026-01-02', 'reviews': 0}}
            learn.save_state(state, path)
            self.assertEqual(learn.read_state(path), state)
            for bad in ('{broken', '[]', '{"task": {"due": "bad", "reviews": 0}}',
                        '{"task": {"due": "2026-01-01", "reviews": -1}}'):
                path.write_text(bad)
                with self.assertRaises(ValueError):
                    learn.read_state(path)
                self.assertEqual(path.read_text(), bad)

    def test_invalid_selectors_cannot_execute_arbitrary_files(self):
        for selector in ('../learn.py', '/tmp/arbitrary.py', '99/01', '00', '0/0'):
            with self.subTest(selector=selector), self.assertRaises(ValueError):
                learn.resolve(selector)

    def check_source(self, source, timeout=1):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'exercise.py'
            path.write_text(source)
            return learn.run_check(path, timeout=timeout)

    def test_feedback_for_wrong_answer_and_stub(self):
        ok, message = self.check_source("assert 1 == 2, 'expected two'\nprint('ok')\n")
        self.assertFalse(ok)
        self.assertIn('expected two', message)
        ok, message = self.check_source('raise NotImplementedError\n')
        self.assertFalse(ok)
        self.assertIn('Next function', message)

    def test_hung_exercise_is_stopped(self):
        ok, message = self.check_source('while True: pass\n', timeout=0.15)
        self.assertFalse(ok)
        self.assertIn('Stopped after', message)

    def test_ok_before_crash_is_not_a_pass(self):
        self.assertFalse(self.check_source("print('ok')\nraise ValueError('broken')\n")[0])
        self.assertFalse(self.check_source("print('hello')\n")[0])
        self.assertTrue(self.check_source("assert 2 + 2 == 4\nprint('ok')\n")[0])

    def test_optimized_parent_still_runs_assertions(self):
        with tempfile.TemporaryDirectory() as directory:
            p = Path(directory) / 'wrong.py'
            p.write_text("assert False, 'must fail'\nprint('ok')\n")
            code = f'import learn; print(learn.run_check(learn.Path({str(p)!r}))[0])'
            result = subprocess.run([sys.executable, '-O', '-c', code], cwd=learn.ROOT,
                                    capture_output=True, text=True, timeout=5)
            self.assertEqual(result.returncode, 0)
            self.assertEqual(result.stdout.strip(), 'False')

    def test_failed_cli_check_does_not_record_progress(self):
        with patch.object(learn, 'read_state', return_value={}), \
             patch.object(learn, 'run_check', return_value=(False, 'try again')), \
             patch.object(learn, 'save_state') as save:
            self.assertEqual(learn.main(['check', '00/01']), 1)
            save.assert_not_called()

    def test_successful_cli_check_records_progress(self):
        with patch.object(learn, 'read_state', return_value={}), \
             patch.object(learn, 'run_check', return_value=(True, 'passed')), \
             patch.object(learn, 'save_state') as save:
            self.assertEqual(learn.main(['check', '00/01']), 0)
            self.assertIn(learn.resolve('00/01').relative_to(learn.ROOT).as_posix(), save.call_args.args[0])


class CourseIntegrityTests(unittest.TestCase):
    def test_learning_path_and_chapters_are_reachable(self):
        self.assertEqual(len(learn.CORE), len(set(learn.CORE)))
        for selector in learn.CORE:
            path = learn.resolve(selector)
            self.assertTrue(path.is_file())
        for chapter in learn.ROOT.glob('[0-9][0-9]_*'):
            self.assertTrue((chapter / 'README.md').is_file())
            self.assertTrue((chapter / 'CHECKPOINT.md').is_file())
            self.assertFalse((chapter / 'solutions').exists())

    def test_document_links_resolve(self):
        for path in learn.ROOT.rglob('*.md'):
            if '.git' in path.parts:
                continue
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text()):
                if '://' not in target and not target.startswith('#'):
                    self.assertTrue((path.parent / target.split('#')[0]).exists(), f'{path}: {target}')

    def test_exercises_remain_questions_with_executable_checks(self):
        for path in learn.exercises():
            tree = ast.parse(path.read_text())
            doc = ast.get_docstring(tree)
            self.assertTrue(doc and 'Problem:' in doc, str(path))
            self.assertTrue(any(isinstance(n, ast.Assert) for n in ast.walk(tree)), str(path))
            self.assertTrue(any(isinstance(n, ast.If) and '__name__' in ast.unparse(n.test)
                                for n in tree.body), str(path))


if __name__ == '__main__':
    unittest.main()
