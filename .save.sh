#! /bin/bash

git add .
git commit -m "$(head -n 1)"
git push -u origin master
