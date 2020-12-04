#!/bin/sh
set -e
changedFiles=$(git diff --cached --name-only --diff-filter=ACM | grep '\.m\?[t]s\?$' | tr '\n' ' ')
[ -z "$changedFiles" ] && exit 0

echo "$changedFiles" | xargs npx prettier --write
echo "$changedFiles" | xargs git add
