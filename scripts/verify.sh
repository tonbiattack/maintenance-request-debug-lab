#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$root"
pnpm typecheck
pnpm test
PYTHONPATH=api python3 -m unittest discover -s api/tests -v
python3 -m compileall -q api/app
git diff --check
for file in README.md DESIGN.md SUMMARY.md coverage-matrix.md docs/git-history.md; do test -f "$file"; done
for id in M01 M02 M03 M04 M05 M06 M07 M08 M09 M10 M11 M12; do test -f "docs/issues/$id.md"; test -f "solutions/$id.md"; done
