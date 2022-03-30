#!/bin/bash

filename='words.txt'
sed -e 's/[^A-Za-z]/ /g' $filename | tr 'A-Z' 'a-z' | tr ' ' '\n' | grep -v '^$' | sort | uniq -c | sort -rn | awk '{t=$1;$1=$2;$2=t;print;}'

# 192. Word Frequency
# https://leetcode.com/problems/word-frequency/
#
# Runtime: 174 ms, faster than 9.47% of Bash online submissions for Word Frequency.
# Memory Usage: 3.8 MB, less than 31.93% of Bash online submissions for Word Frequency.

# declare -A store

# n=1
# while read line; do
#   echo "Line No. $n : $line"
#   n=$((n+1))
#   IFS=' ' read -r -a array <<< "$line"
#   for index in "${!array[@]}"
#   do
#     echo "$index ${array[index]}"
#     echo store[$array[$index]]
#     echo "${store[array[index]]+_}"
#     if [ ${store[array[index]]+_} ]; then
#       store[$array[$index]]=store[$array[$index]]+1
#     else
#       store[$array[$index]]=1
#     fi
#   done
# done < $filename
# for k in "${!store[@]}"; do
#   echo "$k $store[$k]"
# done