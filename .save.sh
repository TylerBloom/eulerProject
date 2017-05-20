#! /bin/bash

git add .
echo "Enter your commit message:"
git commit -m "$(head -n 1)"
git push -u origin master
