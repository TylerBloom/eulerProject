#! /bin/bash

cat .problem099.data | gawk -F "," '{print $1,"\n",$2}' | ./.problem099.py
