#! /bin/bash

cat .problem022.data | sed 's/"//g' | sed 's/,/\n/g' | ./.problem022Sort.py | ./.problem022.py

