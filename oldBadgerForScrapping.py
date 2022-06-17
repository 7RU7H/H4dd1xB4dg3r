import multiprocessing as mp
import threading, os, sys, time, dataclasses, subproccess
# import workspace_management internalise it in the class

# slots break in multiple inheritance AVOID, 20% efficiency over no slot dict
@dataclass(slots=True)
class Target:
    organisation_root: str    
    domain_root: str
    cidr_range: str
    domain_name: str
    # TODO BIG DESIGN CHOICES
    #domain_name_list: dict - listing in text file is good for tools, !!
    # TODO 
    ansnum: dict 
    #out-of-scope-related
    #blacklisted_domains: #TODO figure it out!!
    #blacklisted_subdomains #TODO figure it out!!!
    blacklist_gospider: str
    project_name_path: str
    project_name: str
    badger_location: str

    def __init__(self):    
        badger_location = os.pwd
        blacklist_gospider = "jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt"

    async def run_sequence(*functions: Awaitable[Any]) -> None:
        for function in functions:
            await function

    async def run_parallelism(*functions: Awaitable[Any]) -> None:
        await asyncio.gather(*functions)
    
    # get all ans put into target dict
   
    async def workspace_setup(project_name):
        await run_sequence(
                check_valid_install()
                create_directory_forest()

                )
    
    async def check_valid_install():

    async def create_directory_forest(project_name):
        # All tool names
        # All found URLs
        # All custom wordlists
        # All stardardised wordlists -> transform
        # All logs
        # Domain_map
        # Domain_wordlist mapping


    async def populate_workspace():

    def new_directory_tree(directory_path):
        os.mkdir()
         
        
    def check_out_of_scope():

    # TODO refactor to one function, concat_domainnames, concat_urls!


    def screenshotting():
    #EyeWitness


        # reconftw, osmedeus in parallel to main
        # Modularity to be recursively run
        # BUT also neatly using bandwidth while dataprocessing  
        # Strategic Nuclei, fuzzing scans   
        # 
        #
        # [osmedeus]                                                                                            | C |
        #                    [nuclei][nuclei]    [nuclei]                                                       | O |
        #  mainchain ->[OSINT][DOMAIN] [SUBDOMAIN] [SERVER]/[EXPLOITATION]                                      | N |
        # [reconftw]    |  [datahandle]   [datahandle]                                                          | S |
        #               |             |                 |                                                       | O |
        #               |           [re:Enumeration-Cycle]                                                      | L |
        #               |       [The fuzziest branch that is queued sequence of fuzz but not the main branch]   | I |
        #               |                                                                                       | D |
        # recursiveMAIN |->[OSINT]-+>[DOMAIN]-+>[SUBDOMAIN]-+>[SERVER]/[EXPLOITATION]                           | A |
        #                                                                                                       | T |
        #                                                                                                       | I |
        #                                                                                                       | O |
        #                                                                                                       | N |
        #


    async def run():
        await run_sequence(
                #scope_init_bbscope()
                await run_parallelism(
                    all_reconftw()
                    all_osmedeus()
                    await run_sequence(
                    # maintool chain block, all black run_(parallel/sequence) beloew each block for legiability 


                    # bruteforcing with amass need parallel main branch dont actually want to wait for this
                    # Similar functions for fuff and wfuzz need to be spread *intelligently - i.e filesize of fuzz wordlist threshhold, parallel 
                    # Or have a queue that is sequenctial fuzzs target
                    )
                # Once first main is concluded as secondary scan on !!leaf-most!! collected information is started - NOT TO BE CONFUSED BY PARALLEL Secondary internal AFTER EACH [MODULE] on itself's collected data.
                # more than that would be overkill and the secondary is more likely to be slower anyway
                    await run_sequence(


                        )
                # Absolute consolidation OR another scan on next newest !!leaf-most!! data
            )


#TODO
#scope related functions
#async def 
        
# reconftw Framework
async def all_reconftw(self.domain_name, output_path):
    process = subprocess.Popen(["/opt/reconftw/reconftw.sh", "-d {domain_name} -a -o reconftw/{time.time}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"reconftw -all scan completed on {domain_name}, check {output_path}")
# osmedeus framework 
async def all_osmedeus():
    process = subprocess.Popen(["osmedeus", "-f extensive -t {domain_name} "], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"reconftw -all scan completed on {domain_name}, check {output_path}")


#
# OSINT
#


# theHarvester
# -s for shodan
async def osint_theHarvester(target,output_path):
    print(f"Beginning theHarvester {target}")
    process = subprocess.Popen(["theHarvester", "-d {target} -g -r -f {output_path} --screenshot {output_path}" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"theHarvester OSINT against {target} complete, check {output_path}")

# recon-ng
async def osint_reconNG(target,output_path):
    print(f"Beginning recon-ng {target}")
    process = subprocess.Popen(["recon-cli", "-d {target} -g -r -f {output_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"recon-ng cli OSINT against {target} complete, check {output_path}")


#
# Aquistion Recon 
#
async def acquistion_recon_wordlist_generation():
    #scrap crunchbase, wiki, google
    # GO GO GO


async def acquisition_recon_Amass_ORG(Target.organisation_root, output_path, log_path):
    print("Beginning Amass intel -org")
    process = subprocess.Popen(["amass", "intel -src -org {Target.organisation_root} -max-dns-queries 2500 -oA {output_path} -{logpath}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Amass intel -src -org complete")

async def acquisition_recon_Amass_CIDR(Target.cidr_range, output_path, log_path):
    print("Beginning Amass intel -src -cidr {}")
    process = subprocess.Popen(["amass", "intel -src -cidr {Target.cidr_range} -max-dns-queries 2500 -oA {output_path} -l {log_path}" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Amass intel -src -cidr complete")

#
# Acquistion Recon Utility
#
async def acqRec_Util_amass_ans_out(intel_output_path, outpath_file):
    print("Getting ASN number from amass intel output")
    process = subprocess.Popen(["scripts/script_amassASN_util.sh", "{intel_output_path} {output_file}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("File containing ASN numbers for amass intel -asn completed")

# cat $1 awk -F, '{print $1}' ORS=',' | sed 's/,$//' | xargs -P3 -I@ -d ',' > $2


async def acqRec_Util_concatenate_domain_names():
    # scrap new domains
    # newdomains -> secondary_list
    # newdomains -> big_list
    # TODO refactor to one function!

await run_sequence(
    await run_parallelism(
    # scrapping acquisition recon function(S?)
    acquisition_recon_Amass_ORG()
    acquisition_recon_Amass_CIDR()
        )
     await run_parallelism(
         acqRec_Util_amass_ans_out()
         acqRec_Util_concatenate_domain_names()
         )
     )


#
# ANS enumeration
#
async def ans_enumeration_Amass(Target.asnum, output_path, log_path):
    for ans in Target_asnum:
        print("Beginning Amass intel -ans {ans} -oA {output_path} -l {log_path}")
        process = subprocess.Popen(["amass", "intel -asn {asn} -max-dns-queries 2500 -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print("Amass intel -asn {asn} complete")
    print(f"Ans recon for {Target.asnum} completed")

#
# ANS enumeration Utility
#
async def ansEnum_Util_concatenate_domain_names():
    # scrap new domains
    # newdomains -> secondary_list
    # newdomains -> big_list
    # TODO refactor to one function!

await run_sequence(
        ans_enumeration_Amass()
        ansEnum_Util_concatenate_domain_names()
        )

#
# Reverse whois
#
# DomLink
# Test usefulness/duration as to whether jsut single domain or domain.txt->{domain}
async def reverse_whois_DOMLink(output_path):
    # Get an API key from WHOXY.com
    # Set that API key in a file named domLink.cfg in the same directory.
    
    #for target in :
        print("Beginning reverseWHOIS with Domlink")
        process = subprocess.Popen(["python /opt/DomLink/domLink.py","-D {target} -o {output_path}" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        #print("")
    print(f"ReverseWHOIS Recon with DomLink completed")

#
#   Rever whois Utility
# 
async def revWhois_Util_concatenate_domain_names():
        # scrap new domains
        # newdomains -> secondary_list
        # newdomains -> big_list
        # TODO refactor to one function!

await run_sequence(
        reverse_whois_DOMLink()
        revWhois_Util_concatenate_domain_names()
        )


###########################################
#
# Analyse relationships
#
###########################################


async def analyse_relationships():
    #scrap builtwith.com/relationship

async def analyse_relationships_findrelationships(project_name, badger_location, target):
    print("findrealtionships.py Started")
    if target.contains(".txt"):
        process = subprocess.Popen(["scripts/script_findrelationships_multi.sh", "{project_name} {badger_location} {target}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
    else:
        process = subprocess.Popen(["python3", "{badger_location}/scripts/findrelationships.py {target 0> {project_name}/findrelationships/findrelationships_output.txt", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
    print("findrelationships.py completed")

# #!/bin/bash
# cat $3 | python3 $2/scripts/findrelationships.py 0> $1/findrelationships/findrelationships_output.txt"

###########################################
#
#  Dorking - SCRAPPAGE! 
#
###########################################

async def dork_target_xtext():
    #Scrap Copyright, Privacy, Terms of service Test
    #uniq with Generics of each, 

#
# Domain Enuemration
#
# Prelimiary domain/subdomain list building
async def domain_enumeration_Assetfinder(domain):
    print("Assetfinder Started")
    process = subprocess.Popen(["assetfinder", "{domain} 0> assetfinder_output.txt", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Assetfinder completed")

# Historic domain/subdomain list building
async def domain_enumeration_Waybackurls():
    print(f"Running independent waybackurls")      
    process = subprocess.Popen(["scripts/script_waybackurl.sh", "{target_list}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Completed independent waybackurls")   

# Bash script to run this, due to subprocess.open([ARG,ARG]):
# This one does go to stdout
#    cat $1 | waybackurls > waybackurl_out.txt



#
# Domain Enuemration Utility
#
async def domEnum_Util_concatenate_urls():   
        # scrap new domains
        # newdomains -> secondary_list
        # newdomains -> big_list
        # TODO refactor to one function!



await run_sequence(
    await run_parallelism(
        domain_enumeration_Waybackurls()
        domain_enumeration_Assetfinder()
    )
    domEnum_Util_concatenate_urls()
)

# Nuclei
async def subdomain_takeover_Nuclei(target):
    if target.contains(".txt"):
        targetstr = f"-list {target}"
    else:
        targetstr = f"-u {target}"        
    print(f"Running Nuclei with the target flag and arguments set to: {targetStr}")   
    process = subprocess.Popen(["nuclei", "{targetStr} -me nuclei/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Completed Nuclei against {targetStr}")


#
# Subdomain Bruteforcing
#

#async def subdomain_bruteforcing_WordlistGen(): - hmm

async def subdomain_bruteforcing_ShuffleDNS():

#domain_name must be a .txt file
async def subdomain_Amass_Non_Brute(domain_name, output_path, log_path, blacklist):
    if blacklist.Contains(".txt"):
        blacklistStr = f"-blf {blacklist}"
    else:
        blacklistStr = f"-bl {blacklist}"
    print("Beginning Amass enum -active -ip -src -df {domain_name} {blacklistStr} -oA {output_path} -l {log_path}")
    process = subprocess.Popen(["amass",  "enum -active -ip -src -df {domain_name} {blacklistStr} -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Amass enum -active -ip -src -df {domain_name} {blacklistStr} -oA {output_path} -l {log_path} complete")


#domain_name must be a .txt file
async def subdomain_Amass_Brute(domain_name, output_path, log_path, blacklist_domains, blacklist_subdomains):
    if blacklist_domains != "":
        blacklistStr = f"-bl {blacklist_domains}"
    if blacklist_subdomains != "":
         blacklistStr = f"-blf {blacklist_subdomains}"
    print(f"Beginning Amass enum -active -ip -src -brute -df {domain_name} {blacklistStr} -oA {output_path} -l {log_path}")
    process = subprocess.Popen([" amass", "enum -active -ip -src -brute {domain_name} {blacklistStr} -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Amass enum -active -ip -src -brute {domain_name} {blacklistStr} -oA {output_path} -l {log_path} complete")
 

#
# Subdomain Bruteforcing Utility
#
# Consoldate list between each tool to improve
# final bruteforcing
await def subdomain_consolidate_lists():


await run_sequence(
            subdomain_bruteforcing_ShuffleDNS()
            subdomain_consolidate_lists()
            subdomain_Amass_Non_Brute()
            subdomain_consolidate_lists()
            subdomain_Amass_Brute()
            )

#
# Subdomain Enumeration
#

# For quick site mapping
# Web crawler needed to brute force and parse sitemap.xml, parse robots.txt, Link Finder
# Gets URLs from Wayback Machine, Common Crawl, Virus Total, Alien Vault
# Finds AWS-S3 from response source
# Finds subdomains from response source
# Generates and verifies links from JavaScript files         
async def subdomain_enumeration_Gospider(target, blacklist, output_path):
        if blacklist != "":
            blacklistStr = f"--blacklist {blacklist}"
        if url.contains(".txt"):
            siteStr = f"-S {target}" # sites file.txt
        else:
            siteStr = f"-s {target}" # site domain
        print(f"Running Gospider against {siteStr} with {blacklistStr}")      
        process = subprocess.Popen(["gospider", "{siteStr} -a --subs --sitemap --robots --js {blacklistStr} -o {output_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"Completed Gospider against {siteStr} with {blacklistStr}")   
        # TODO
        # Must Reappraise wordlists and artifacts

# Hakrawler for JS endpoints
async def subdomain_enumeration_Hakrawler(url_list, output_path):
    print("Beginning Hakrawler script")
    process = subprocess.Popen(["scripts/script_hakrawler.sh", "{url_list} {output_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()    
    print(f"Complete Hakrawler on {url_list} check {output_path}")
#

# #!/bin/bash 
# cat $1 | hakrawler 0> $2 

#Subdomainizer to analyse JS
async def subdomain_enumeration_Subdomanizer():


# Take a list of domains and probe for working HTTP and HTTPS servers 
async def subdomain_enumeration_Httprobe(target_list):
    print(f"Running httProbe")      
    process = subprocess.Popen(["scripts/script_httprob.sh", "{target_list}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Completed httProbe")   

# Bash script to run this, due to subprocess.open([ARG,ARG]):
#    cat $FILE | httprobe -c 50 0> httprobe_out.txt

async def subdom_Util_gospider(input_path):
    print(f"")      
    process = subprocess.Popen(["scripts/script_gospiderSD.sh", "{input_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"")    

# Bash script to run this, due to subprocess.open([ARG,ARG]):
#grep -r -Eo '(http|https)://[^/"]+' $@ | anew
# add to subdomain lists

await run_parallelism(
    subdomain_enumeration_Gospider()
    subdomain_enumeration_Hakrawler()
    subdomain_enumeration_Subdomanizer()
    subdomain_enumeration_Httprobe()
    )

###########################################
#
#   Subdomain Scrapping 
#
# ALMOST CERTIANLY MAKE THIS ONE GOLANG PIPE 
# BEWARE LOTS STRING OPERATIONS AND LOOKUP AND UNIQ AFTER SCRAPPING
# 

#shosubgo, when I get shodan key
#async def subdomain_scrapping():

#subscraper requires api key
async def subdomain_scrapping_Subscraper():

async def subdomain_scrapping_Amass():

async def subdomain_scrapping_Subfinder():



# github subdomain scraps github
# kingofbugbounty tips
# Search subdomains using github and httpx
# Github-search - Using python3 to search subdomains, httpx filter hosts by up status-code response (200)
async def subdomain_scrapping_GithubSubdomain(api_key_github, domain, output_path):
    print(f"Beginning github-subdomain targeting {domain}")
    process = subprocess.Popen(["","{api_key_github} {domain} {output_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Completed github-subdomain")
#!/bin/bash
# python3 /opt/github-subdomain.py -t $1 -d $2 | httpx --title > $3
   
await run_parallelism(
        subdomain_scrapping_GithubSubdomain()
        )
#
#
#
# 
########################################


#Cloudbrute
async def cloud_enumeration_Cloudbrute():

###########################################
#                                       -> Data processing -> Further Recon
#   Port Analysis -> Service Scanning -+> Brutespray
#
###########################################

async def port_analysis_Dnmasscan():
    exit_code = subprocess.call(.scripts/dnmasscan.sh) # FLAGS

async def port_analysis_Util_Pass_dnmascan_out():

async def port_analysis_Masscan(ip_ranges, exclude, output_path)
    if exclude.Contains(".txt"):
        excludeStr = f"--excludefile {exclude}"
    else:
        excludeStr = ""
    if ip_range.Contains(".txt"):
        with open(ip_range, "r") as f:
            ips = f.read()
            for target in ips:
                print(f"Masscan using file:{ip_ranges}, target: {target}")
                process = subprocess.Popen(["masscan", "-p0-65535 --rate 10000000 {excludeStr} -oG {output_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                process.wait()
                print(f"Masscan against {target} complete")
    else:
        print(f"Masscan using file:{ip_ranges}, target: {target}")
        process = subprocess.Popen(["masscan", "-p0-65535 --rate 10000000 {excludeStr} -oG {output_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"Masscan against {target} complete")



async def port_analysis_Util_Pass_masscan_out():

async def service_scanning_Nmap():
    #output from masscan
    #nmapScriptGun
    #nmap service scanning

async def service_scanning_Brutespray():

await run_sequence(
        port_analysis_Dnmasscan()
        port_analysis_Util_Pass_dnmascan_out()
        port_analysis_Masscan()
        port_analysis_Util_Pass_masscan_out()
        service_scanning_Nmap()
        )

# service_scanning_Brutespray()



############################################
#
#   Web Scanning
#
############################################
#TODO -port flag
#
async def web_scanning_Nikto(target_list, output_path):
    with open(target_list , "r") as f:
        urls = f.read()
        for target in urls:
            print(f"Starting Nikto scanning on {target}")
            process = subprocess.Popen(["nikto", "-h {target} -C all -o {output_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            process.wait()
            print(f"Finished Nikto scanning on {target}")
        print(f"Finished all Nikto scanning within {target_list}")



# TODO MORE flags https://github.com/Hackmanit/Web-Cache-Vulnerability-Scanner/tree/master
async def web_scanning_Web_Cache_Vulnerability_Scanner(json_report):
    with open(target_list , "r") as f:
        urls = f.read()
        for target in urls:
            print(f"Testing potential webcache poisioning with Web-Cache-Vulnerability-Scanner: {target}")
            process = subprocess.Popen(["wcvs", "--reclimit 1 -gr -gp {json_report} -ej" ]stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            process.wait()
            print(f"Completed testing of potential webcache poisioning with Web-Cache-Vulnerability-Scanner: {target}")
        print(f"Finished all Web-Cache-Vulnerability-Scanner scanning within {target_list}")

# NOT SURE ON quality of this 
# TODO Review source code, need stdout, would need multiple runs -is it even worth it? 
async def web_scanning_analyze_FEJS_libraries_Is_website_vulnerable(domain_name, protocol):
    print(f"")
    process = subprocess.Popen(["is-website-vulnerable", "{target} --json --js-lib --desktop"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    process = subprocess.Popen(["is-website-vulnerable", "{target} --json --js-lib --mobile"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"")

async def vuln_osmedeus(target_list):
    with open(target_list , "r") as f:
        urls = f.read()
        for target in urls:
            print(f"osmedeus Vulnerablity scan starting against {target}")
            process = subprocess.Popen(["osmedeus", "-f extensive-vuln -t {target} "], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            process.wait()
            print(f"osmedeus Vulnerablity scan completed for {target}")
        print(f"Finished all Osmedeus Vuln scanning within {target_list}")

#
# Web scanning Utility
#
# GENERAL NOTE TODO THESE WILL ALMOST CERTAINLY END UP AS WRAPPERS OR APP IN GO
# FOR The superior parsing
#

async def webscan_Util_Nikto_report(nikto_output):
        print(f"Compiling Nikto report for Nikto scans {nikto_output}")
        process = subprocess.Popen(["reportNikto.go", "{nikto_output}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"Completed Nikto Report! Please MANAULLY review at {process}")

async def webscan_Util_gron_wcvs():
    # recursively gron the wcvs output 


await run_sequence(
    await run_parallelism(
        web_scanning_Nikto()
        web_scanning_Web_Cache_Vulnerability_Scanner()
        web_scanning_analyze_FEJS_libraries_Is_website_vulnerable()
        vuln_osmedeus()
        )
    webscan_Util_gron_wcvs()
    webscan_Util_Nikto_report()
    
    
)

# def webscan_optional_wpscan():


###########################################
#
#   Exploitation
#
###########################################

# Vulnerablity found in data processing
# class contruction exploit_target
# switch depending of expo type: xxs, sqli, ssrf

async def fuzz_SSRF_SSRFmap():



# jason haddix sqli statistics paper database nomanclature "id"
async def sql_database_found_SQLMAP():






async def report():
    amass viz -d3 domains.txt -o 443 /your/dir/
    amass viz -maltego domains.txt -o 443 /your/dir/  # If end up using it
    amass viz -visjs domains.txt -o 443 /your/dir/


# Consider use cases later see github useages
# https://github.com/tomnomnom/gron
async def json_analysis_Gron():

async def get_urls_Meg():

async def dostuffwith_Concurl():


async def techstack_analysis_TechStack():
    process = subprocess.Popen(["/opt/TechStack.sh", "{}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()


#favfreak
async def favicon_analysis_Favfreak():



###########################################
#
# 
#
###########################################


# ffuf

# wfuzz 

