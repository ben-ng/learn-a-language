#!/bin/bash

# FS is the field seperator
# NF is the number of fields
# $i is a variable variable
awk '{FS="[^a-zA-Z]+"; for(i=1;i<=NF;i++) if (match($i, "^[a-zA-Z]+$")) printf "%s\n", tolower($i);}' 2cities.txt |\
sort | uniq -c | sort -n | tail -rn $1
