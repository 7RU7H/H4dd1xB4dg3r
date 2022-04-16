# H4dd1xB4dg3r
Automated Bug Bounty Recon Setup

# Overview
The H4dd1xB4dg3r is an automated bug bounty recon suite named after: 
Jason Haddix []()  
It a project started to improve my golang, python and ehtical hacking toolset. The reasoning for the naming being that leetication and mashing of the primary influence's name and honey badgers. Honey rhymes with money and honey badgers find honey. It is my starting out personal bug hunting repository that will be inspired by Daniel Messler, InsiderPHD, HakLuke, NahamSEc and Jason Haddox talks I have watched. If had handfist any naming of tools related to them with other bug hunting animals and cyber security concept, atleast the goal of having fun designing and testing this modularly is accomplished.

My rational for using python over golang is simply to migitate any garbage collector issues that could occur as this project could cynically be thought of a multiprocessing wrapper for other people's hard work. Therefore because there is alot of data moving around in and out of the Hadd1xB4gd3r during runtime and that bug bounty automation will scale in runtime time and data process - plus garbage collection equates to sad me. I love golang, but also need to up my python game for hacking, network automation generally and a future hope move toward deep-learning security tooling. And currently golang does not get official support from tensorflow or memory control and writing this in C would probably leave never starting bug hunting this anytime soon. Golang will be used for wordlist building related tasks as string package, parsing buffers, etc is faster in golang apperently, also those taskes have defined conclusion to their runtime meeting my generally stingy memory usage criteria.

So it nix pipeline of modular scripts/bins using opensource tools only or my own custom go, python, bash scripts and tools.
It is motivated by the hope to find some bugs for fun, accolade and profit in that order.
The control flow similar to the sections of questions to ask at various stages for bug hunting.
This heavily inspired from talks Bug Hunters methodologyv4, various automation, tool usage talks, articles by Daniel Messlier.

# Looking for, maybe make 
scope checker  
subdomain scraping Cloud ranges bash script  
https://github.com/projectdiscovery/wappalyzergo  
https://labs.detectify.com/2021/11/30/hakluke-creating-the-perfect-bug-bounty-automation/  
consider https://github.com/cure53/Flashbang.git

# Todo
tomnomnom wordlist building   
check:
https://github.com/jhaddix/tbhm  
nuclei templating https://github.com/projectdiscovery/nuclei  
https://hakluke.com/blog/  
https://github.com/projectdiscovery/httpx  
https://github.com/tomnomnom/hacks  
https://github.com/tomnomnom?tab=repositories&q=&type=&language=&sort=stargazers
https://github.com/hakluke/haktrails - "echo google.com | haktrails subdomains | httpx | hakrawler"

https://github.com/s0md3v/Arjun
https://github.com/m4ll0k/SecretFinder
https://github.com/m4ll0k/BBTz


CEwl and wordlistctl

Daniel Messler Masscan guide -DONE
consider:   
https://github.com/jhaddix/domain  
https://github.com/jhaddix/megplus  


# THE PLAN:

# Controlflow and Paralellism
                                                                        -> scrapping -> usability -> curation -> 
                                                    -> main branch(recon -> (wordlist io) && vulnscanning && fuzz/bruteforcing)
setup/checking -> initialise\_workspace -> mainflow -> all\_reconftw
						    -> all_osmedeus

# Wordlists
https://github.com/danielmiessler/SecLists  
https://github.com/danielmiessler/RobotsDisallowed


# OSINT

[theHarvester](https://www.kali.org/tools/theharvester/)
[recon-ng](https://www.kali.org/tools/recon-ng/)

# Scope Domains

## Url building
 
## Wordlist making
[unfurl](https://github.com/tomnomnom/unfurl)
## Check then Fetch


## Acquistions Recon
[theHarvester](https://github.com/laramies/theHarvester)
    crunchbase, wiki google
## ASN Enumeration
http://bgp.he.net
[amass](https://github.com/OWASP/Amass)
## ReverseWHOIS
Whoxy.com 
register for free api key
beware: rever whois data as it is least high fidelity source of new root/seed domains - may include parked domains or redirect that are out of scope
[DOMLink](https://github.com/vysecurity/DomLink)
## AD/Analytic Relationship
    builtwith.com/relationships
## Dorking
    Copyright Text
    Terms of service text
    Privacy policy text
## Shodan
     is twitch.amazon.eu relevant for testing?

# Domain Enumeration
Assetfinder: Find domains and subdomains related to a given domain 
[assetfinder](https://github.com/tomnomnom/assetfinder)

waybackurls fetches all the URLs that the Wayback Machine knows about for a domain *BUT other repo do this better and with other stuff*
this is jsut to separate output for wordlists as well as timings 
[waybackurl](https://github.com/tomnomnom/waybackurls)


# SubDomain Enumeration
1.Linked and JS discovery
1.Subdomain Scraping -> ++
1.Subdomain Bruteforce 

gospider and hakrawler both do similar things I will see what produces the best stuff or best maintained
[gospider](https://github.com/jaeles-project/gospider)
[hakrawler](https://github.com/hakluke/hakrawler)
[Subdomainizer](https://github.com/nsonaniya2010/SubDomainizer?)
analysises JS  

# Subdomain scrapping
Subdomain Scraping Sources are coming out all the time
Infrastructure Sources
Certificate Sourtce
Security Sources
Search Engines

[subscraper](https://github.com/m8r0wn/subscraper)
subcraping recursively scrapes 
requires:
Censys.io (API Key required https://search.censys.io/register)

amass again!

[subfinder](https://github.com/projectdiscovery/subfinder)

scrape github for subdomains
[github-subdomains](https://github.com/gwen001/github-subdomains)

[shosubgo](https://github.com/incogbyte/shosubgo)
https://developer.shodan.io/api/requirements
```
go run /shosubgo/main.go -d target.com -s YourAPIKEY
```


# Server Enumeration
https://github.com/projectdiscovery/httpx

# Cloud
[cloudbrute](https://github.com/jhaddix/CloudBrute)
```
CloudBrute -d target.com -k target -m storage -t 80 -T 10 -w "./data/storage_small.txt"
CloudBrute -d target.com -k keyword -m storage -t 80 -T 10 -w -c amazon -o target_output.txt
```
# Subdomain bruteforcing

Use good Wordlist:
https://github.com/assetnote/commonspeak2-wordlists
Create target specific Wordlists
```
amass enum -brute -d $DOMAIN -src
amass enumer -bute -d $DOMAIN -rf resolvers.txt -w bruteforce.list
```
[shuffledns](https://github.com/projectdiscovery/shuffledns)

# Alteration Scanning
[altdns](https://github.com/infosec-au/altdns)
```
altdns -i subdomains.txt -o data_output -w words.txt -r -s results_output.txt
```
# Web scanning 
Nikto



# TechStack Analysis
[TechStack](https://github.com/danielmiessler/TechStack)

# JSON analysis
Gron makes JSON greppable! 
[gron](https://github.com/tomnomnom/gron)

# Favicon Analysis
[favfreak](https://github.com/devanshbatham/FavFreak)
Requires CHECK installation!
```
cat urls.txt | python3 favfreak.py -o output
```
# Port Analysis

[dnmasscan](https://github.com/rastating/dnmasscan)
dsmasscan example.txt dns.log -p80,443 -oG masscan.log

Masscan only scans IPS get from the command above!
[masscan](https://github.com/robertdavidgraham/masscan)
```
masscan -p80,8000-8100 10.0.0.0/8 2603:3001:2d00:da00::/112
# dump current confi and exits, can be fed as input back 
masscan -p80,8000-8100 10.0.0.0/8 2603:3001:2d00:da00::/112 --echo > xxx.conf
masscan -c xxx.conf --rate 1000
# haddix
masscan -p0-65535 -iL $ipFile --maxRate 1800 -oG $outputFile.log
```
## Service Scanning 
masscan -> nmap service scan -< brutespray
python3 //brutespray.py --file /nmap.gnmap


# SubdomainTakeover
[can-i-take-over-xyz](https://github.com/EdOverflow/can-i-take-over-xyz)

[nuclei](https://github.com/projectdiscovery/nuclei)

# Interlace

# Webscanning 
[jaeles](github.com/jaeles-project/jaeles)
nikto

# Screenshotting

[EyeWitness](https://github.com/FortyNorthSecurity/EyeWitness)

# Frameworks



Buckets
GithubLeaks


# Installation
```
install.sh
```

# Old but not forgotten
This section is just a reminder of stuff I tried or found better but may return to



#### Gone but there anyway

I like grep
# https://github.com/tomnomnom/gf)
#go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest

#httprobe takes a list of domains and probe for working HTTP and HTTPS servers - REPLACED WITH httpx
# [httprobe](https://github.com/tomnomnom/httprobe)
