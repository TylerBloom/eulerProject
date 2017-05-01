#! /bin/bash

cat p022_names.txt | sed 's/"//g' | sed 's/,/\n/g' | ./sortProblem022.py | ./problem022.py

