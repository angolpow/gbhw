#!/usr/bin/env bash

mkdir -p 20{10..17}/{01..12}
for i in {2010..2017}
do
  for j in {01..12}
  do
    for k in {001..003}
    do
      echo "File $k" > $i/$j/$k.txt
    done
  done
done
