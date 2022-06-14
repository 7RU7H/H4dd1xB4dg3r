#!/bin/bash


badger_location=$(pwd)
organisation=$1
project_name=$2

# target is placeholder for protocol/address|domain/port

# Acquistition recon & ANS enumeration
amass intel -org $organisation -max-dns-queries 2500 | awk -F, '{print $1}' ORS=',' | sed 's/,$//' | xargs -P3 -I@ -d ',' amass intel -asn @ -max-dns-queries 2500''
wait

# Domain name grep into array

# osint with theHarvester
theHarvester -d $domain -g -r -f $theHavester_output
wait

# reverseWHOIS
python3 /opt/DomLink/domLink.py -D $target -o $domlink_output
wait

# analyse relationships
cat $organisation | python3 $badger_location/scripts/findrelationships.py target 0> $project_path/findrelationships/findrelationships_output.txt
wait

# domain enumerations
#assetfinder
assetfinder $domain 0> assetfinder_output.txt
wait

# waybackmachine
$badger_location/scripts/script_waybackurl.sh
wait

# github

# subdomain takeover
NUCLEI_targetstr="-list $" #TODO
nuclei $targetStr -me $project_path/nuclei-$target
wait

# subdomain brute forcing
amass enum -active -ip -src -df $domain_name $AMASS_blacklistStr -oA $project_path/amass_enum_output -l $amass_log_path
wait

# subdomain enumeration

gospider -d 0 -s $target -a -d 5 -c 5 --subs --sitemap --robots --js --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt  -o $gospider_output/$target
wait
grep -r -Eo '(http|https)://[^/"]+' $gospider_output/ | anew 

# subdomain scrapping

# port analysis
scripts/dnmasscan.sh
scripts/dnsmasscanToMasscan.sh # TODO
masscan -p0-65535 --rate 1000 $masscan_excludeStr -oG $masscan_output
nmap #TODO
    #output from masscan
    #nmapScriptGun
    #nmap service scanning

# webservice scan 
nikto -h $target -o $output_path
wait

# Last 
osmedeus -f extensive-vuln -t $target
wait
