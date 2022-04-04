import multiprocessing as mp
import threading, os, sys, time, dataclasses, subproccess

# A class to store out of scope targets to test against for safety while hunting
@dataclass(slots=True)
class Target_Out_Of_Scope:

    def __init__(self):

# slots break in multiple inheritance AVOID, 20% efficiency over no slot dict
@dataclass(slots=True)
class Target:
    organisation_root: str    
    domain_root: str
    cidr_range: str
    domain_name: str
    domain_name_list: dict
    ansnum: dict 

    def __init__(self):
    

    async def run_sequence(*functions: Awaitable[Any]) -> None:
        for function in functions:
            await function

    async def run_parallelism(*functions: Awaitable[Any]) -> None:
        await asyncio.gather(*functions)

    def check_out_of_scope():

    def screenshotting():
    #EyeWitness

    async def run():
        # reconftw
        # Modularity to be recursively run
        # BUT also neatly using bandwidth while dataprocessing  
        # Strategic Nuclei scans   
        #                           [nuclei]    [nuclei] 
        # [mainchain]->[OSINT][DOMAIN] [SUBDOMAIN] [SERVER]/[EXPLOITATION]
        #       [reconftw]       [datahandle]   [datahandle]
        

@dataclass(slots=True)
class Project:
    project_name_path: str
    project_name: str
    
    def __init__(self):
    
    
    async def check_valid_install():

    async def workspace_setup(project_name):
        os.mkdir(project_name)



# Protocols!!! management


###########################################
#
# reconftw Framework - parallel
#
###########################################

async def all_reconftw(self.domain_name, output_path):
    process = subprocess.Popen(["/opt/reconftw/reconftw.sh", "-d {domain_name} -a -o reconftw/{time.time}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"reconftw -all scan completed on {domain_name}, check {output_path}")

###########################################
#
# Aquistion
#
###########################################

async def acquistion_recon():
    #scrap crunchbase, wiki, google

async def acquisition_recon_Amass():
    print("Beginning Amass intel -org")
    process = subprocess.Popen(["amass", "intel -src -org {Target.organisation_root}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Amass intel -src -org complete")
    print("Beginning Amass intel -src -cidr")
    process = subprocess.Popen(["amass", "intel -src -cidr {Target.cidr_range}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Amass intel -src -cidr complete")

###########################################
#
# ANS enuemration
#
###########################################


async def ans_enumeration_Amass():
    print("Beginning Amass intel -ans")
    process = subprocess.Popen(["amass intel -asn {Target.asnnum}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print("Amass intel -asn complete")

###########################################
#
# reverse whois
#
###########################################
  
async def reverse_whois_DOMLink():
    #DOMLink


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



###########################################
#
# Domain Enuemration
#
###########################################

# Prelimiary domain/subdomain list building
async def domain_enumeration_Assetfinder():
    assetfinder <domain>

# Historic domina/subdomain list building
async def domain_enumeration_Waybackurls():
    cat domains.txt | waybackurls > urls


await run_parallelism(
    domain_enumeration_Waybackurls()
    domain_enumeration_Assetfinder()
    )

# Take a list of domains and probe for working HTTP and HTTPS servers 
async def domain_enumeration_Httprobe():
    cat domains.txt | httprobe -c 50



###########################################
#
# Nuclei
#
###########################################


#nuclei
async def subdomain_takeover_Nuclei():
    # flag -u or -list
    # target = {protocol}://{target}
    # target = {urllist}.txt
    process = subprocess.Popen(["nuclei", "{flag} {target} -me nuclei/{target}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()


###########################################
#
# Subdomain Bruteforcing
#
###########################################


async def subdomain_bruteforcing_WordlistGen():

async def subdomain_bruteforcing_ShuffleDNS():

async def subdomain_bruteforcing_Amass():
    amass enum -ip -src -d {domain_name}
    amass enum -ip -src -brute { 



###########################################
#
# Subdomain Enumeration
#
###########################################

# For quick site mapping
async def subdomain_enumeration_Gospider():

# Hakrawler for JS endpoints
async def subdomain_enumeration_Hakrawler():

#Subdomainizer to analyse JS
async def subdomain_enumeration_Subdomanizer():


await run_parallelism(
    subdomain_enumeration_Gospider()
    subdomain_enumeration_Hakrawler()
    subdomain_enumeration_Subdomanizer()
    )

# Take a list of domains and probe for working HTTP and HTTPS servers 
async def subdomain_enumeration_Httprobe():
    cat domains.txt | httprobe -c 50




###########################################
#
#   Subdomain Scrapping 
#
###########################################

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
