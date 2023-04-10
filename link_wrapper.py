#!python

import sys
import subprocess

unused_libs = ["userenv.lib", "legacy_stdio_definitions.lib", "bcrypt.lib"]

args = []
for x in sys.argv:
    if x in unused_libs:
        continue
    args.append(x)

args[0] = "LINK.EXE"

r = subprocess.run(args, capture_output=True)
print(r.stdout.decode(errors='replace').replace('\uFFFD', '?'))
print(r.stderr.decode(errors='replace').replace('\uFFFD', '?'), file=sys.stderr)
sys.exit(r.returncode)

# sys.exit(subprocess.run(args, encoding="raw_unicode_escape").returncode)
