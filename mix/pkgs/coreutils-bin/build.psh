mkcd $out/bin
untar $src/coreutils-*
set files coreutils/*/bin/*

---
import os

for f in files:
    n = os.path.basename(f)

    if n[0] == 'g':
        os.symlink(f, n[1:])
---
