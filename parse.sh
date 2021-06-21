#!/bin/sh

SCRIPTPATH="$(dirname $(readlink -f "$0"))"
cd "$SCRIPTPATH"

[ ! -e fmt.py ] && cp default-fmt.py fmt.py

grep -o '##ENOLOGMESSAGE .*' | cut -d' ' -f2- | python3 fmt.py
