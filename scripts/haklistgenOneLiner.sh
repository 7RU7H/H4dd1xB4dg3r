#!/bin/bash
# https://github.com/KingOfBugbounty/KingOfBugBountyTips
subfinder -silent -d domain | anew subdomains.txt | httpx -silent | anew urls.txt | hakrawler | anew endpoints.txt | while read url; do curl $url --insecure | haklistgen | anew wordlist.txt; done
cat subdomains.txt urls.txt endpoints.txt | haklistgen | anew wordlist.txt;
