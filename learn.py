"""Small, local learning queue. Python 3.10+, standard library only."""
import argparse
from datetime import date, timedelta
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
STATE = ROOT / '.learning-progress.json'
# A short first lap. The rest stays available in the chapter library.
CORE = [
    '00/01', '00/02', '00/05', '00/03', '00/04', '00/06',
    '03/01', '05/02', '05/01', '04/01', '04/04', '06/01',
    '06/02', '06/06', '07/01', '10/01', '08/01', '11/01',
    '11/04', '12/01', '13/01', '14/01', '15/01',
]


def exercises(root=ROOT):
    return sorted(root.glob('[0-9][0-9]_*/problems/*.py'))


def resolve(selector, root=ROOT):
    paths = exercises(root)
    parts = selector.split('/')
    if len(parts) == 2 and all(p.isdigit() for p in parts):
        matches = [p for p in paths if p.parent.parent.name.startswith(parts[0].zfill(2) + '_')
                   and p.name.startswith(parts[1].zfill(2) + '_')]
    else:
        matches = [p for p in paths if p.relative_to(root).as_posix() == selector]
    if len(matches) != 1:
        raise ValueError('Choose an exercise such as 00/01. Use: python learn.py list')
    return matches[0]


def read_state(path=STATE):
    if not path.exists():
        return {}
    try:
        state = json.loads(path.read_text())
        if not isinstance(state, dict):
            raise ValueError()
        for key, item in state.items():
            if not isinstance(key, str) or not isinstance(item, dict):
                raise ValueError()
            date.fromisoformat(item['due'])
            if type(item['reviews']) is not int or not 0 <= item['reviews'] <= 3:
                raise ValueError()
        return state
    except (ValueError, TypeError, KeyError):
        raise ValueError(f'{path.name} is unreadable. Back it up and rename it before restarting; it has not been overwritten.')


def save_state(state, path=STATE):
    temp = path.with_suffix('.tmp')
    temp.write_text(json.dumps(state, indent=2) + '\n')
    temp.replace(path)


def record_pass(state, key, today=None):
    today = today or date.today()
    # Repeated runs today must not push a due review into the future.
    if key not in state:
        state[key] = {'due': (today + timedelta(days=1)).isoformat(), 'reviews': 0}


def record_review(state, key, today=None):
    today = today or date.today()
    if key not in state:
        raise ValueError('Run and pass the exercise checks before recording a recall review.')
    if state[key]['due'] > today.isoformat():
        raise ValueError('That review is not due yet. You can practise without changing its date.')
    stage = min(state[key]['reviews'] + 1, 3)
    state[key] = {'due': (today + timedelta(days=(3, 7, 14)[stage - 1])).isoformat(), 'reviews': stage}


def run_check(path, timeout=5):
    try:
        # -O would remove the assert checks. Always launch a normal child interpreter.
        result = subprocess.run([sys.executable, str(path)], capture_output=True, text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return False, f'Stopped after {timeout:g}s. Trace one loop: which variable changes and when does it stop?'
    if result.returncode == 0 and result.stdout.strip().endswith('ok'):
        return True, 'Checks passed. Now explain why it works and invent one extra edge case.'
    lines = result.stderr.splitlines()
    if 'NotImplementedError' in result.stderr:
        return False, 'Next function is still waiting for you. Implement one small piece, then run this again.\n' + '\n'.join(lines[-4:])
    detail = '\n'.join(lines[-5:]) or result.stdout[-600:] or 'The file did not finish with ok.'
    return False, 'Needs another try. Compare the expected result with your hand trace:\n' + detail


def today_task(state, root=ROOT, today=None):
    today = today or date.today()
    valid = {p.relative_to(root).as_posix() for p in exercises(root)}
    due = sorted((v['due'], k) for k, v in state.items() if k in valid and v['due'] <= today.isoformat())
    if due:
        return 'Recall review', root / due[0][1]
    for selector in CORE:
        p = resolve(selector, root)
        if p.relative_to(root).as_posix() not in state:
            return 'Next small step', p
    return None, None


def show_task(state):
    kind, path = today_task(state)
    if path is None:
        print('First lap complete. Choose a chapter in ROADMAP.md; keep reviewing what you know.')
        return
    key = path.relative_to(ROOT).as_posix()
    print(f'{kind}: {path.stem[3:].replace("_", " ")}')
    print(f'Read: {path.parent.parent.name}/README.md\nOpen: {key}')
    print('Five minutes is enough to start: read the question and trace one example.')
    print(f'Check: python learn.py check {key}')
    if kind == 'Recall review':
        print('Cover your code. Explain the approach, then rewrite it on paper or in a scratch file.')
        print(f'After successful recall: python learn.py reviewed {key}')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    subs = parser.add_subparsers(dest='command')
    subs.add_parser('today', help='one next task (default)')
    subs.add_parser('list', help='browse the optional full exercise library')
    check = subs.add_parser('check', help='run one exercise with a time limit')
    check.add_argument('exercise')
    review = subs.add_parser('reviewed', help='record an honest closed-book recall review')
    review.add_argument('exercise')
    args = parser.parse_args(argv)
    try:
        if args.command == 'list':
            for p in exercises():
                print(p.relative_to(ROOT).as_posix())
            return 0
        state = read_state()
        if args.command in (None, 'today'):
            show_task(state)
            return 0
        p = resolve(args.exercise)
        key = p.relative_to(ROOT).as_posix()
        if args.command == 'reviewed':
            record_review(state, key)
            save_state(state)
            print('Review saved. Next recall: ' + state[key]['due'])
            return 0
        passed, message = run_check(p)
        print(message)
        if passed:
            record_pass(state, key)
            save_state(state)
        return 0 if passed else 1
    except (ValueError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
