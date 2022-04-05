import multiprocessing as mp
import threading, os, sys, time, dataclasses, subproccess

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
    project_name_path: str
    project_name: str

    def __init__(self):    

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


# Aquistion Recon 
async def acquistion_recon():
    #scrap crunchbase, wiki, google

async def acquisition_recon_Amass_ORG(Target.organisation_root, output_path, log_path):
    print("Beginning Amass intel -org")
    process = subprocess.Popen(["amass", "intel -src -org {Target.organisation_root -oA {output_path} -{logpath}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Amass intel -src -org complete")

async def acquisition_recon_Amass_CIDR(Target.cidr_range, output_path, log_path):
    print("Beginning Amass intel -src -cidr {}")
    process = subprocess.Popen(["amass", "intel -src -cidr {Target.cidr_range} -oA {output_path} -l {log_path}" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Amass intel -src -cidr complete")

#
# Acquistion Recon Utility
#
async def acqRec_util_amass_ans_out(amass_output_path):

async def acqRec_util_concatenate_domain_names():
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
         acqRec_util_amass_ans_out()
         acqRec_util_concatenate_domain_names()
         )
     )



#
# ANS enumeration
#
async def ans_enumeration_Amass(Target.asnum, output_path, log_path):
    for ans in Target_asnum:
        print("Beginning Amass intel -ans {ans} -oA {output_path} -l {log_path}")
        process = subprocess.Popen(["amass", "intel -asn {asn} -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print("Amass intel -asn {asn} complete")
    print(f"Ans recon for {Target.asnum} completed")

#
# ANS enumeration Utility
#
async def ansEnum_util_concatenate_domain_names():
    # scrap new domains
    # newdomains -> secondary_list
    # newdomains -> big_list
    # TODO refactor to one function!

await run_sequence(
        ans_enumeration_Amass()
        ansEnum_util_concatenate_domain_names()
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
async def revWhois_util_concatenate_domain_names():
        # scrap new domains
        # newdomains -> secondary_list
        # newdomains -> big_list
         # TODO refactor to one function!

await run_sequence(
        reverse_whois_DOMLink()
        revWhois_util_concatenate_domain_names()
        )


###########################################
#
# Analyse relationships
#
###########################################


async def analyse_relationships():
    #scrap builtwith.com/relationship

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
async def domain_enumeration_Assetfinder():
    print("Assetfinder Started")
    process = subprocess.Popen(["assetfinder", "{domain} 0> assetfinder_output.txt", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Assetfinder completed")

# Historic domina/subdomain list building
async def domain_enumeration_Waybackurls():
    print(f"Running indenpendent waybackurls")      
    process = subprocess.Popen(["script_waybackurl.sh", "{target_list}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Completed independent waybackurls")   

# Bash script to run this, due to subprocess.open([ARG,ARG]):
# This one does go to stdout
#    cat $FILE | waybackurls > waybackurl_out.txt



#
# Domain Enuemration Utility
#
async def domEnum_concatenate_urls():   
        # scrap new domains
        # newdomains -> secondary_list
        # newdomains -> big_list
        # TODO refactor to one function!



await run_sequence(
    await run_parallelism(
        domain_enumeration_Waybackurls()
        domain_enumeration_Assetfinder()
    )
    domEnum_concatenate_urls()
)


    




# Nuclei
async def subdomain_takeover_Nuclei(target):
    targetStr = ""
    if target.contains(".txt"):
        targetStr = f"-list {target}"
    else:
        targetStr = f"-u {target}"        
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
    blacklistStr = ""
    if blacklist_domains != "":
        blacklistStr += "-bl " + blacklist_domains
    if blacklist_subdomains != "":
         blacklistStr += "-blf " + blacklist_subdomains
    print("Beginning Amass enum -active -ip -src -df {domain_name} {blacklistStr} -oA {output_path} -l {log_path}")
    process = subprocess.Popen(["amass",  "enum -active -ip -src -df {domain_name} {blacklistStr} -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Amass enum -active -ip -src -df {domain_name} {blacklistStr} -oA {output_path} -l {log_path} complete")


#domain_name must be a .txt file
async def subdomain_Amass_Brute(domain_name, output_path, log_path, blacklist_domains, blacklist_subdomains):
    blacklistStr = ""
    if blacklist_domains != "":
        blacklistStr += "-bl " + blacklist_domains
    if blacklist_subdomains != "":
         blacklistStr += "-blf " + blacklist_subdomains
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
        siteSingleFlag = "-s " # site    
        siteListFlag = "-S " # sites
        blacklistFlag = "--blacklist " # blacklist
        blacklistStr = ""
        siteStr = ""
        if blacklist != "":
            blacklistStr += blacklistFlag + blacklist
        if url.contains(".txt"):
            siteStr += siteListFlag + target
        else:
            siteStr += siteSingleFlag + target

        print(f"Running Gospider against {siteStr} with {blacklistStr}")      
        process = subprocess.Popen(["gospider", "{siteStr} -a --subs --sitemap --robots --js {blacklistStr} -o {output_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"Completed Gospider against {siteStr} with {blacklistStr}")   
        # TODO
        # Must Reappraise wordlists and artifacts

# Hakrawler for JS endpoints
async def subdomain_enumeration_Hakrawler():

#Subdomainizer to analyse JS
async def subdomain_enumeration_Subdomanizer():


# Take a list of domains and probe for working HTTP and HTTPS servers 
async def subdomain_enumeration_Httprobe(target_list):
    print(f"Running httProbe")      
    process = subprocess.Popen(["script_httprob.sh", "{target_list}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Completed httProbe")   

# Bash script to run this, due to subprocess.open([ARG,ARG]):
#    cat $FILE | httprobe -c 50 0> httprobe_out.txt




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

#subscrapper requires api key
async def subdomain_scrapping_Subscrapper():

async def subdomain_scrapping_Amass():

async def subdomain_scrapping_Subfinder():

#github-subdomain scraps github
async def subdomain_scrapping_GithubSubdomain():
   
await run_parallelism(
        subdomain_scrapping_GithubSubdomain()
        )

#
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
    exit_code = subprocess.call(./dnmasscan.sh) # FLAGS

async def port_analysis_PASS_dnmascan_out():

async def port_analysis_Masscan():

async def port_analysis_PASS_masscan_out():

async def service_scanning_Nmap():
    #output from masscan
    #nmapScriptGun
    #nmap service scanning

async def service_scanning_Brutespray():

await run_sequence(
        port_analysis_Dnmasscan()
        port_analysis_PASS_dnmascan_out()
        port_analysis_Masscan()
        port_analysis_PASS_masscan_out()
        service_scanning_Nmap()
        service_scanning_Brutespray()
        )


############################################
#
#   Web Scanning
#
############################################
#TODO -port flag
#
async def web_scanning_Nikto(protocol, target, project_name):
    process = subprocess.Popen(["nikto", "-h {protocol}://{target} -c -o {project_name}/nikto/"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()

# flags https://github.com/Hackmanit/Web-Cache-Vulnerability-Scanner/tree/master
async def web_scanning_Web_Cache_Vulnerability_Scanner(domain_name, protocol):
    print(f"Testing potential webcache poisioning with Web-Cache-Vulnerability-Scanner: {protocol}://{domain_name}")
    process = subprocess.Popen(["wcvs", ""]stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Completed testting of potential webcache poisioning with Web-Cache-Vulnerability-Scanner: {protocol}://{domain_name}")


async def web_scanning_analyze_FEJS_libraries_Is_website_vulnerable(domain_name, protocol):
    process = subprocess.Popen(["npx is-website-vulnerable" "{protocol}://{domain_name} [--json] [--js-lib] [--mobile|--desktop] [--chromePath] [--cookie] [--token]]", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()

async def vuln_osmedeus(target):
    print(f"osmedeus Vulnerablity scan starting against {target}")
    process = subprocess.Popen(["osmedeus", "-f extensive-vuln -t {target} "], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"osmedeus Vulnerablity scan completed")

await run_parallelism(
    web_scanning_Nikto()
    web_scanning_Web_Cache_Vulnerability_Scanner()
    web_scanning_analyze_FEJS_libraries_Is_website_vulnerable()
    vuln_osmedeus()
    )


###########################################
#
#   Exploitation
#
###########################################

# Vulnerablity found in data processing
# class contruction exploit_target
# switch depending of expo type: xxs, sqli, ssrf

async def fuzz_SSRF_SSRFmap():

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
