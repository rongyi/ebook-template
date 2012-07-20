#! /bin/bash

sed -i 's/&/\\&/g' $1
sed -i 's/%/\\%/g' $1
sed -i 's/_/\\_/g' $1

sed -e '/^[0-9]\+$/d' $1
sed -e '/^'"$2"'$/d' $1
sed -e 's/。$/。\r/' $1

