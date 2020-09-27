#!/usr/bin/env bash

files=`find . -maxdepth 1 -type f`

for file in $files
do
  owner=`stat -c %U $file`
  if [ ! -d $owner ]
  then
    mkdir $owner
    chown $owner $owner
  fi

  cp -p $file $owner/
done
