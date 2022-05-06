
read project_name -p "Provide a project name:"
organisation=""

# initial osmedeus
osmedeus -f extensive -t https://$domain_name 
wait

# osint
theHarvester -d $target -g -r -f $theHavester_output

# Acquistition recon & ANS enumeration
amass intel -org $organisation -max-dns-queries 2500 | awk -F, '{print $1}' ORS=',' | sed 's/,$//' | xargs -P3 -I@ -d ',' amass intel -asn @ -max-dns-queries 2500''

# reverseWHOIS
python3 /opt/DomLink/domLink.py -D $target -o $domlink_output

# analyse relationships
cat $ | python3 $badger_location/scripts/findrelationships.py target 0> $project_name/findrelationships/findrelationships_output.txt

# domain enumerations
assetfinder $domain 0> assetfinder_output.txt
scripts/script_waybackurl.sh


# github

# subdomain takeover
NUCLEI_targetstr="-list $" #TODO
nuclei $targetStr -me $project_name/nuclei-$target

# subdomain brute forcing
amass enum -active -ip -src -df $domain_name $AMASS_blacklistStr -oA $output_path -l $log_path

# subdomain enumeration

gospider -d 0 -s $target -a -d 5 -c 5 --subs --sitemap --robots --js --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt  -o $gospider_output/$target
# find all the links
grep -r -Eo '(http|https)://[^/"]+' $gospider_output/ | anew 

# subdomain scrapping


# port analysis
scripts/dnmasscan.sh
scripts/dnsmasscanToMasscan.sh # TODO
masscan -p0-65535 --rate 10000000 $masscan_excludeStr -oG $masscan_output
nmap #TODO
    #output from masscan
    #nmapScriptGun
    #nmap service scanning

# webservice scan 
nikto -h $target -c -o $output_path

# Last 
osmedeus -f extensive-vuln -t $target
