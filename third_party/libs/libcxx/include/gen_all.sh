#!/bin/sh

find . | grep -v 'gen_all' | grep -v '__' | grep -v 'exper' | grep -v 'support' | grep -v 'module' | sort | sed -e 's/\.\//#include "/' | while read line; do echo $line\"; done
