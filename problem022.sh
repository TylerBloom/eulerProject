#! /bin/bash

cat p022_names.txt | sed 's/"//g' | sed 's/,/\n/g' | ./problem022Sort.py | ./problem022.py

