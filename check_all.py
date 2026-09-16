"""Run every chapter's exercises (your progress) or solutions (proves the tests are sound).

  python check_all.py              # your progress, one line per chapter
  python check_all.py solutions    # every reference solution must pass
"""
import pathlib
import subprocess
import sys

which = "solutions.py" if len(sys.argv) > 1 and sys.argv[1] == "solutions" else "exercises.py"
root = pathlib.Path(__file__).parent
ok = True
for chapter in sorted(p for p in root.iterdir() if p.is_dir() and (p / which).exists()):
    out = subprocess.run([sys.executable, which], cwd=chapter, capture_output=True, text=True)
    last = (out.stdout.strip().splitlines() or [out.stderr.strip()[-200:] or "no output"])[-1]
    print(f"{chapter.name:36} {last}")
    if which == "solutions.py":
        a, _, b = last.partition("/")
        ok &= a.isdigit() and a == b.split()[0]
sys.exit(0 if ok else 1)
