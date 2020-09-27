#!/usr/bin/env bash

# проверяем аргумент
if [ $# != 1 ]
then
  echo Usage:
  echo $0 file
  exit 1
fi

# через tr
# создаем новый файл tr_имя_файла с искомым содержимым
tr -s '\n' < $1 | tr [:lower:] [:upper:] > tr_${1}

# через sed
# создаем новый файл sed_имя_файла с искомым содержимым
sed '/^$/d; s/[a-z]/\U&/g' $1 > sed_${1}
