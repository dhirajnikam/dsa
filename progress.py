"""Show one next step; opt into a chapter or full check with 05 or --all."""
import argparse
from learn import ROOT, exercises, read_state, record_pass, run_check, save_state, show_task


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('chapter', nargs='?', help='chapter number, for example 05')
    parser.add_argument('--all', action='store_true', help='run every exercise; may take several minutes')
    args = parser.parse_args()
    if args.chapter and (len(args.chapter) != 2 or not args.chapter.isdigit()):
        parser.error('Use a two-digit chapter such as 05.')
    try:
        state = read_state()
        if not args.chapter and not args.all:
            show_task(state)
            print(f'\n{len(state)} exercises have passed checks. This is practice history, not a readiness score.')
            return 0
        paths = [p for p in exercises() if not args.chapter or p.parent.parent.name.startswith(args.chapter + '_')]
        if not paths:
            parser.error('No such chapter. Choose 00 through 17.')
        passed = 0
        for p in paths:
            ok, message = run_check(p)
            key = p.relative_to(ROOT).as_posix()
            print(f'{"PASS" if ok else "PRACTISE"} {key}: {message}', flush=True)
            if ok:
                record_pass(state, key)
                passed += 1
        save_state(state)
        print(f'\n{passed}/{len(paths)} files passed. Choose one next step, not all unfinished files.')
        return 0 if passed == len(paths) else 1
    except (ValueError, OSError) as error:
        print(error)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
