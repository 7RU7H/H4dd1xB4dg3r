#!/bin/bash
# This script finds the nikto databases the outputs the messages potentially output after a 
# web vulnerability scan and stdouts them to a output.txt file
DB=$(locate nikto/databases/)
for FILE in $DB; do 
	if $FILE != "db_variables" && "db_parked_strings" &&  "db_headers" &&  "db_dictionary" && "db_404_strings"
	then
		case "${FILE}" in
			"db_tests") cat $FILE | awk '{if (FNR>37) print $11}' | uniq >> output.txt;;
			"db_server_msgs") cat $FILE | awk '{if (FNR>18) print $4}' | uniq >> output.txt;;
			"db_realm") cat $FILE | awk '{if (FNR>19) print $5}' | uniq >> output.txt;;
			"db_outdated") cat $FILE | awk '{if (FNR>17) print $4}' | uniq >> output.txt;;
			"db_multiple_index") cat $FILE | awk '{if (FNR>15) print $1}'uniq >> output.txt;;
			"db_httpoptions") cat $FILE | awk '{if (FNR>17) print $4}' | uniq >> output.txt;;
			"db_favicon") cat $FILE | awk '{if (FNR>18) print $3}' | uniq >> output.txt;;
			"db_embedded") cat $FILE | awk '{if (FNR>17) print $5}' | uniq >> output.txt;;
			#"db_drupal") cat $FILE | awk '{if (FNR>19) print $2}' | uniq >> output.txt;;
		       	"db_domino") cat $FILE | awk '{if (FNR>19) print $3}' | uniq >> output.txt;;
			"db_dir_traversal") cat $FILE | awk '{if (FNR>23) print $4}' | uniq >> output.txt;;
			"db_content_search") cat $FILE | awk '{if (FNR>19) print $4}' | uniq >> output.txt;;			
		esac
	fi
done


