#!/bin/bash
# Enumerate character filtering on parametre with curl
target="" # set to target url
chars=()

mkdir /tmp/output
for x in $chars; do
	curl "$url$char" -o /tmp/output/$char
done

# grep and filter by filtered characters
filteredChars=()
echo $filteredChars
