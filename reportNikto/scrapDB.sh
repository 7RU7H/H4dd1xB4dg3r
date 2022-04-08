#!/bin/bash

#some kind of file position shift based off of "#######"

for FILE in $DB; do 
	if $FILE != "db_variables" && "db_parked_strings" &&  "db_headers" &&  "db_dictionary" && "db_404_strings"
	then
		case "${FILE}" in
			"db_tests") awk '{print $11}' | uniq >> output.txt;;
			"db_server_msgs" 
			# osvdb
			# awk '{print 4}' | uniq
			"db_realm") awk '{print 5}' | uniq >> output.txt;;
			"db_outdated") awk '{print $4}' | uniq >> output.txt;;
			#"db_index") awk #seperate by . {


			
		esac
