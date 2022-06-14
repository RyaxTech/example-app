#!/usr/bin/env bash

set -e
# For debug
# set -x

while getopts "fd:" opt; do
  case "$opt" in
    f)
      DO_CHECK_ONLY="false"
      ;;
    d)
      CHECK_DIR="$OPTARG"
      ;;
    ?)
      echo "script usage: $(basename $0) [-f] [-d directory]" >&2
      exit 1
      ;;
  esac
done

TO_CHECK_DIR=${CHECK_DIR:-"."}
CHECK_ONLY=${DO_CHECK_ONLY:-"true"}

if [[ $CHECK_ONLY == "true" ]]
then
    BLACK_EXTRA_OPTS="--check --diff"
    ISORT_EXTRA_OPTS="--check-only --diff"
fi

echo "-- Checking import sorting"
isort -s .venv -s ci --filter-files $ISORT_EXTRA_OPTS $TO_CHECK_DIR

echo "-- Checking python formating"
black $TO_CHECK_DIR --exclude "docs|ci|migrations|.venv|.*pb2.py|.*pb2_grpc.py" $BLACK_EXTRA_OPTS

echo "-- Checking python static checking"
flake8 $TO_CHECK_DIR --exclude="docs/*,ci/*,migrations/*,.venv/*,*pb2.py,*pb2_grpc.py" --per-file-ignores='*/__init__.py:F401'

echo "-- Checking type annotations"
mypy $TO_CHECK_DIR/seedlbrain --exclude '(/*pb2.py)'

echo "-- Checking for dead code"
vulture




