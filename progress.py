"""Score yourself 0..100. Runs every problems/*.py and counts the ones that print ok.

    python progress.py        # all phases
    python progress.py 05     # one phase (prefix match on folder name)
"""
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).parent
prefix = sys.argv[1] if len(sys.argv) > 1 else ""

total = passed = 0
for phase in sorted(p for p in ROOT.iterdir() if p.is_dir() and p.name.startswith(prefix) and p.name[:2].isdigit()):
    files = sorted((phase / "problems").glob("*.py"))
    ok = 0
    for f in files:
        r = subprocess.run([sys.executable, f], capture_output=True, text=True, timeout=30)
        ok += r.returncode == 0 and r.stdout.strip().endswith("ok")
    total += len(files)
    passed += ok
    bar = "#" * ok + "." * (len(files) - ok)
    print(f"{phase.name:<35} {ok:>3}/{len(files):<3} {bar}")

score = round(100 * passed / total) if total else 0
print(f"\nSCORE: {score}/100  ({passed}/{total} problems solved)")
