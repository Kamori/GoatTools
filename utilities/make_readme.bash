#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cp $DIR/../README_TEMPLATE.md $DIR/../README.md

README_TABLE=$($DIR/../venv/bin/python $DIR/goatgen.py --format markdown-table 2>&1)

cat << EOF >> $DIR/../README.md
# Completion Report

$README_TABLE
EOF
