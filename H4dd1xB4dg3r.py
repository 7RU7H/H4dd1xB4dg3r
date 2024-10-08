#!/usr/bin/python
import multiprocessing as mp
import threading, os, sys, time, subprocess, logging, argparse, re, asyncio, signal
from  typing import Any, Awaitable
from dataclasses import dataclass
# import workspace_management internalise it in the class

class print_colors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  WHITE = '\033[97m'
  YELLOW = '\033[93m'
  RED = '\033[91m'
  BLACK = '\033[90m'
  MAGENTA = '\033[95m'
  GREEN = '\033[92m'
  BLUE = '\033[94m'
  CYAN = '\033[96m'

# slots break in multiple inheritance AVOID, 20% efficiency over no slot dict
@dataclass(slots=True)
class Target:
    organisation_root: str    
    domain_root: str
    cidr_range: str
    domain_names_list: list
    domain_names_historic: list
    subdomains_list: list
    subdomains_historic_file_path: str
    ansnum: dict 
    out_of_scope_path: str
    full_path_to_project_dir: str
    project_name: str
    badger_location: str
    toollist: list
    domain_name_file_path: str
    recon_ng_custom_resource_file_exists: bool
    recon_ng_custom_file_checks: bool
    recon_ng_resource_file_path: str
    project_default_parent_path: str
    current_recursion_count: int
    max_recursion_count: int
    non_uniq_domain_names: list

    def __init__(self, args):
        self.organisation_root = args.target_organisation
        self.domain_root = ''
        self.non_uniq_domain_names = []
        self.toollist = ['amass', 'aquatone', 'domLink', 'assetfinder', 'waybackurls', 'theHarvester', 'findrelationships', 'recon-ng']
        self.recon_ng_custom_resource_file_exists = False
        self.recon_ng_custom_file_checks = False
        self.project_default_parent_path = '/tmp'
        self.asnum = {}
        self.ansnum = {}
        self.current_recursive_count = 0
        
        if args.asn != '':
            self.asnnum =+ args.asn 
        else:
            print("It is best practice to start with ASNs that you have manually checked!") 
            print("Beware as an idiot that is non-paying student of Jason Haddix - https://www.youtube.com/watch?v=nGs8pWIj5k4 6:10 - do not automate the ASN recon")
            print("Amass does not check you legal protections, shine your shoes and counter-sue a target!") 

        if args.domain != '':
            print("It is best practice to start with ASNs that you have manually checked!") 
            print("Beware as an idiot that is non-paying student of Jason Haddix - https://www.youtube.com/watch?v=nGs8pWIj5k4 6:10 - do not automate the ASN recon")
            print("Amass does not check you legal protections, shine your shoes and counter-sue a target!") 
            if self.asnnum == '':
                choice = choice_wheel_of_doom("ARE REALLY SURE THAT WANT TO CONTINUE WITHOUT A ASN")
                print("I am sorry you are being stupid")
                os.exit()
        else:
            print("No domains were passed at the command line")

        if args.project_path != '':
            self.full_path_to_project_dir = f"{args.project_path}/"
        else:
            self.full_path_to_project_dir = f"{self.project_default_parent_path}"
        
        if os.path.exists(self.full_path_to_project_dir):
            print(f"Error Invalid project path: {args.project_path}")
            exit(1)
        else:
            self.full_path_to_project_dir += f"{self.project_name}"

        if os.path.exists(): 
            print(f"Error project name already exists: {self.project_default_parent_path}{args.project_name}")
            exit(1)
        else:
            os.mkdir(self.full_path_to_project_dir)
            print(f"Project directory successfully made at: {self.full_path_to_project_dir}")

        self.domain_names_list += args.domain_name
        self.out_of_scope_path = args.out_of_scope_path
        self.recursion_count = args.recursive_osint_count
        self.badger_location = os.exec('pwd')
        
        if args.recon_ng_custom_resource_file != None:
            if path.isfile({args.recon_ng_custom_resource_file}):
                assign_custom_reconng_resource_file()
            if self.recon_ng_custom_file_checks != True:
                print(f"Error Invalid recon_ng custom resource file: {args.recon_ng_custom_resource_file}")
                exit(1)
            else:
                # if custom recon-ng resource file path path set bool and path else default resource file 
                assign_custom_reconng_resource_file()
        else:
            self.recon_ng_custom_resource_file = f"{self.badger_location}/recon-ng/recon-ng-default-resource-file.txt"
        
        if args.recursion_count != '':
            self.max_recursion_count = 0
        else:
            self.max_recursion_count = args.resource_count
        # init tool checks

        create_directory_forest(self.full_path_to_project_dir)
        
    
    # TODO script check and called tool checks seperate
    # Script check and 
    # async def check_valid_install():
    # See newH4dd1x/extract-check-valid-install

    def create_directory_forest(path):
        os.mkdir({path}/log)
        os.mkdir({path}/reports)
        os.mkdir({path}/domainmap)
        os.mkdir({path}/wordlists)
        os.mkdir({path}/wordlists/scrappings)
        os.mkdir({path}/wordlists/custom)
        os.mkdir({path}/wordlists/utility)
        for tool in self.toollist:
            tool_path = f"{path}/{tool}"
            os.mkdir(tool_path)
            for count in self.max_recursion_count:
                count_dir = f"{tool_path}/pass-{str(count)}"
                os.mkdir(count_dir)
        if recon_ng_custom_resource_file_exists and recon_ng_custom_resource_file_exists:
            os.rename("{self.recon_ng_resource_file_path}", "{self.badger_location}/recon-ng/recon-ng-default-resource-file.txt") 
        print(f"Directory forest completed a {path}")

    # TODO
    # Needs STRUCTURING by domain hierarchy!!
    def create_directory_tree_by_address(address, path):
        if address.Contains(".txt"):
            f = open(target_list , "r")
            address_list = f.read()
            for addr in address_list:
                os.mkdir({path}/domainmap/{addr}/wordlists)
        else:
            os.mkdir({path}/domainmap/{address}/wordlists)
        print(f"Directory structure added to {path}/domainmap")

    def update_out_of_scope_file(file):
        print(f"Updating out of scope file {file}")
    
    def map_inital_files(dir):
        print(f"Mapping directory: {dir}")

    def map_recursion_new_domains():
        print(f"Mapping recursively to find new domains in: {dir}")
    
    def map_recursion_new_urls():
        print(f"Mapping recursively to find new urls in: {dir}")
    
    def map_recursion_new_cidr():
        print(f"Mapping recursively to find new CIDR in: {dir}")
    
    def map_recursion_new_files_and_dirs():
        print(f"Mapping recursively to find new all new files in: {dir}")
    
    def updating_out_of_scope_file_handler():
        print("For the sake of legality and judgement, I must insist you check new finding manually incase of scope changes or to updated")
        print("N will then prompt you for how you want to update the out-of-scope.txt file!")
        choice = choice_wheel_of_doom("updating out-of-scope.txt")
        if choice:
            update_out_of_scope_file()
        else:
            print("Something regarding the selection of scope of update the out-of-scope.txt went very wrong")        

    def choice_wheel_of_doom(selectionString):
        while True:
            try:
                acceptance = str(input("[!] Are you sure you want to continue, this script will ask you again - I must insist (Y/N)!"))
                if acceptance == "Y":
                    second_acceptance = str(input("[!] Are you absolutely sure you want to continue - final chance (Y/N)!"))
                    if second_acceptance == "Y":
                        return true
                    else:
                        print(f"Failed Selection for {selectionString} - Return to the infinite loop of safety!")
                        continue
                else:
                    selection_complete = update_out_of_scope_file()
                    if select_complete == False:
                        print(f"Failed Selection for {selectionString} - Return to the infinite loop of safety!")
                        continue
                    else:
                        break
            except ValueError:
                print(f"This script is very insistent on trying to avoid you making some \"{selectionString}\" mistake, please try harder to enter either Y for Yes or N for No")
                continue

    # Filesystem snapshot and comparsion
    # Make new directory

    # TODO - IT MAY BE POSSIBLE THAT PYTHON IS NOT THE ANSWER TO THIS PROBLEM A WRAPPER MAY BE - this a thread of the master play VERY useful for blue and red teaming - Omniserver, Gzhodan - HAIL THE MIGHT GZLOP
    # TODO DO NOT WRITE IT IN PYTHON - WRAP EVERYTHING
    # Added new directories
    # Documenting what changes and additions are made:
    # out-of-scope file, directory structure
    # Make sure that all new data is unique before saving to disks if possible
    # Ensure linear collection to prevent duplicate additions
    # 
    def recusive_handler():
        if self.current_recursion_count != 0:
            update_out_of_scope_file_handler()
            map_recursion_new_files_and_dirs()
            map_recursion_new_domains()
            map_recursion_new_urls()
            map_recursion_new_cidr()
        else:
            map_inital_files()

        
    
    #TODO
    def check_custom_recon_ng_file(filepath): 
        extension_test = False
        if filepath.contains(".txt"):
            extension_test = True

    def assign_custom_reconng_resource_file():
            self.recon_ng_resource_file_path = args.recon_ng_custom_resource_file 
            self.recon_ng_custom_resource_file = True
            self.recon_ng_custom_file_checks = check_custom_recon_ng_file() # TODO
            print(f"Custom resource file accepted and will be moved to {self.project_path}/recon-ng/")


    async def run_sequence(*functions: Awaitable[Any]) -> None:
        for function in functions:
            await function

    async def run_parallelism(*functions: Awaitable[Any]) -> None:
        await asyncio.gather(*functions)
    
    # get all ans put into target dict
   
    async def workspace_setup(project_name):
        await run_sequence(
                # check_valid_install()
                create_directory_forest()
                )
         
    async def check_out_of_scope(url):
        print(f"Checking if {url} is out-of-scope")
        if url.contains("https://"):
            no_proto_url = url[7:]
        else:
            no_proto_url = url[6:]
        tidy_url = no_proto_url.split('/')
        with open(self.out_of_scope_path, "r") as f:
            blacklist = f.read()
            for bl_url in blacklist:
                if bl_url.Contains(tidy_url):
                    print(f"Out-of-scope url {url} found!")
                    return True
        print(f"Out-of-scope url {url} not found")
        return False

    # Faster go version in the works gurl.go
    # fall back if required
    # refactor to new program!
    async def handle_domain_name(domain_name):
        temp_domain = trim_excess_from_domain_name(domain_name)
        if check_uniq_domain_name(temp_domain):
            add_new_domain_name()

    # is (?<=://)(?i)[a-z,.]* better?
    # From https://www.bugcrowd.com/blog/how-to-regex-a-practical-guide-to-regular-expressions-regex-for-hackers/
    async def trim_excess_from_domain_name(url):
        rm_proto_and_dir = str(re.findall(r':\/\/(.[^/]+)', url))
        unlist = rm_proto_and_dir[0]
        dots_split = re.split('[.]', rm_proto_and_dir.strip())
        tld = str(re.sub(r'[^a-z-A-Z0-9 ]', "", dots_split[-1]))
        result = f"{str(dots_split[-2])}.{tld}"
        return result

    async def check_uniq_domain_name(domain_name):
        if self.non_uniq_domain_names.contains(domain_name):
            add_new_domain_name_to_records()
        # else: check the queue and remove any that QUEUE 
                
    async def add_new_domain_name_to_records():
        with open(self.domain_names_file_path, "a") as f:
            f.write(domain_name)
            self.domain_names_historic += domain_name
            print(f"Added a new domain name: {domain_name}")

    
    # From each util_concatenation function
    # a instance of gurl will take one file of a list of filenames passed into the util function and perform 
    # faster than grep greppage of urls and then formats and appends them if fileexists or create the file if it does not
    # It takes -u {urltype} for formating to, -i {input_file} -o {output_file} {-a}
    async def gurl_url_list_concatenation(url_format_type, input_path, output_path, append_flag):
        print(f"Beginning gurl_url_list_concatenation {input_path} with formatting options {url_format_type}")
        if append_flag != None:
            print(f"Handling cli gurl.go with append flag, appending to an existing output file {output_path}")
        process = subprocess.Popen(["gurl", "-u {url_format_type} -i {input_path} -o {output_path} {append_flag}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"The url formating and concatentation of gurl.go with {url_format_type} extracted from {input_path} can be found {output_path}")


    # TODO consider how to consolidate
    # TODO smart recursion so that it does not retread entirely but not only endpoints
    
    # TODO refactor to one function, concat_domainnames, concat_urls!
    
    # OSINT
    # theHarvester
    # -s for shodan
    async def osint_theHarvester(target, output_path):
        print(f"Beginning theHarvester against {target}")
        process = subprocess.Popen(["theHarvester", "-d {target} -v -n -g -r -f {output_path} --screenshot {output_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"theHarvester OSINT against {target} complete, check {output_path}")

    async def osint_recon_ng(resource_file, target, output_path):
        print(f"Beginning Recon-NG against {target}")
        process = subprocess.Popen(["recon-cli", "-r {resource_file}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"Recon-NG OSINT against {target} check {output_path}")

    def shodanSelection():
        print("This function is here to the set flags and provide information")
        print("Shodan is powerful")
        print("For information regarding Shodan for recon: https://www.youtube.com/watch?v=4CL_8GRNVTE shodan-cli")
        print("Shosbugo https://github.com/incogbyte/shosubgo - grab subdomain using shodan api")
        

    # Acquistion Recon 
    #async def acquisition_recon_wordlist_generation():
        #scrap crunchbase, wiki, google
        # GO GO GO

    # TODO
    # Breakpoint -> certian scopage 
    # Pause, modify?
    # Pause get data by manual cmd running, check data

    # TODO
    # Beware as an idiot that is not a paying student of Haddix - https://www.youtube.com/watch?v=nGs8pWIj5k4 6:10 - do not automate the ASN recon
    # Multiple companies that are named that same thing!!! 
    # Enjoy Scope : and not NoScoping yourself! Future me

    # Print commands
    # curl hurricane electric's internet serivces site: bgp.hg.net
    # provide organisation name

    # echo $ASN | asnmap -sient | naabu -silent  - optional naabu hellscape nmap-cli 
    # OR 
    # Stealth do `smap` https://github.com/s0md3v/Smap - uses nmap syntax! does not need a shodan key, but uses shodan!

   


    # TODO
    # Certificate DBs.. 
    # IS is big company or is it tiny company in the cloud
    # certificates
    # echo | openssl s_client -servername hostname -connect $domainORIP:443 2>/dev/null | openssl x509 -outform PEM > $customCERT.crt
    # CloudRecon https://github.com/g0ldencybersec/CloudRecon Finding assets from certificates! Scan the web
    # Parse out subdomains:
    # `grep -F '.$DOMAIN.$TLD' cloudrecon.txt | awk -F'[][]' '{print $2}' | sed 's# #\n#g | grep ".$DOMAIN.$TDL" | sort -fu | cut -d ',' -f1 | sort -u`
    # Parse out all domains
    # `grep -F '.$DOMAIN.$TLD' cloudrecon.txt | awk -F'[][]' '{print $2}' | sed 's# #\n#g | sort -fu | cut -d ',' -f1 | sort -u`
    
    # CloudRecon Backup - http://kaeferjaeger.gay - they scan sites every 3 weeks ~

    # CONSIDER THE DOMAINS, before proceeding 

    # TODO
    # Certs
    # prips -- print the IP addresses in a given range - debian/ubuntu apt
    # https://github.com/hakluke/hakip2host    
    # `prips IP/CIDR | hakip2host`


    async def acquisition_recon_Amass_ORG(output_path, log_path):
        print("Beginning Amass intel -org")
        process = subprocess.Popen(["amass", "intel -src -org {self.organisation_root} -max-dns-queries 2500 -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print("Amass intel -src -org complete")

    async def acquisition_recon_Amass_CIDR(output_path, log_path):
        print("Beginning Amass intel -src -cidr {}")
        process = subprocess.Popen(["amass", "intel -src -cidr {self.cidr_range} -max-dns-queries 2500 -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print("Amass intel -src -cidr complete")
    # Acquistion Recon Utility
    # cat $1 awk -F, '{print $1}' ORS=',' | sed 's/,$//' | xargs -P3 -I@ -d ',' > $2
    async def acqRec_Util_amass_find_ans(intel_output_path, outpath_file):
        print("Getting ASN number from amass intel output")
        process = subprocess.Popen(["scripts/script_amassASN_util.sh", "{intel_output_path} {output_file}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print("Dictionary containing ASN numbers constructed")

    # ANS enumeration
    async def ans_enumeration_Amass(output_path, log_path):
        print("Beginning Amass ANS enumeration")
        for asn in self.asnum:
            print("Beginning Amass intel -ans {asn} -oA {output_path} -l {log_path}")
            process = subprocess.Popen(["amass", "intel -asn {self.asnum} -max-dns-queries 2500 -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            process.wait()
            print("Amass intel -asn {asn} complete")
        print(f"Ans recon for asnum dictionary completed")

    # ANS enumeration Utility
    #async def ansEnum_Util_concatenate_domain_names():
        # scrap new domains
        # newdomains -> secondary_list
        # newdomains -> big_list
        # TODO refactor to one function!  


    # Reverse whois with DomLink
    # Get an API key from WHOXY.com
    # Set that API key in a file named domLink.cfg in the same directory.
    async def reverse_whois_DOMLink(target_list, output_path):
        print("Beginning reverseWHOIS with Domlink")
        with open(target_list , "r") as f:
            targets = f.read()
            for target in targets:
                print("Performing reverseWHOIS with Domlink against {target}")
                process = subprocess.Popen(["python /opt/DomLink/domLink.py","-D {target} -o {output_path}" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                process.wait()
                print(f"ReverseWHOIS for {target} with DomLink completed")
        print(f"ReverseWHOIS Recon with DomLink completed")

    # Reverse whois Utility
    #async def revWhois_Util_concatenate_domain_names():
            # scrap new domains
            # newdomains -> secondary_list
            # newdomains -> big_list
            # TODO refactor to one function!


    # Analyse relationships
    # async def analyse_relationships():
        #scrap builtwith.com/relationship

    # Target must be a file
    # cat $3 | python3 $2/scripts/findrelationships.py 0> $1/findrelationships/findrelationships_output.txt"
    async def analyse_relationships_findrelationships(project_name, badger_location, target_list):
        print("Findrealtionships.py Started")
        with open(target_list , "r") as f:
            targets = f.read()
            for target in targets:
                process = subprocess.Popen(["scripts/script_findrelationships_multi.sh", "{path}/{project_name} {badger_location} {target}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                process.wait()
                print(f"Findrelationships.py completed analysis of {target}")
        print("Findrelationships.py completed")


    # Dorking - SCRAPPAGE!
    # async def dork_target_xtext():
        #Scrap Copyright, Privacy, Terms of service Test
        #uniq with Generics of each, 

    # Domain Enuemration
    # Prelimiary domain/subdomain list building
    async def domain_enumeration_Assetfinder(targets, output_path):
        print("Assetfinder Started")
        with open(target_list , "r") as f:
            targets = f.read()
            for target in targets:
                process = subprocess.Popen(["assetfinder", "{target} 0> {output_path}/assetfinder_output.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                process.wait()
                print(f"Assetfinder analysis against {target}")
        print("Assetfinder completed")

    # Historic domain/subdomain list building
    async def domain_enumeration_Waybackurls(targets, output_path):
        print(f"Running independent waybackurls")      
        process = subprocess.Popen(["scripts/script_waybackurl.sh", "{targets} {output_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"Completed independent waybackurls")   

    # Bash script to run this, due to subprocess.open([ARG,ARG]):
    # This one does go to stdout
    #    cat $1 | waybackurls >> $2/waybackurl_out.txt

    # Domain Enumeration Utility
    # async def domEnum_Util_concatenate_urls():   
            # scrap new domains
            # newdomains -> secondary_list
            # newdomains -> big_list
            # TODO refactor to one function!

    # Domain Flyerover with screenshots
    async def aquatone_flyover(input_path, output_path):
        print(f"Running Aquatone with listing {input_path}")      
        process = subprocess.Popen(["scripts/aquatoneEverything.sh", "{input_path} {output-path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"Completed Aquatone flyover with {input_path}")   


    # cat $1 | aquatone -out $2/aquatone


 
    async def run():
        await run_sequence(
                #scope_init_bbscope()
                    await run_parallelism(
                        osint_theHarvester(),
                        osint_recon_ng(),
                        # scrapping acquisition recon function(S?)
                        # metabigor!!
                        await run_sequence(
                            acquisition_recon_Amass_ORG(),
                            acquisition_recon_Amass_CIDR(),
                            await run_parallelism(
                                acqRec_Util_amass_find_ans(),
                                acqRec_Util_concatenate_domain_names(),
                             ),
                            await run_parallelism(
                                await run_sequence(
                                    ans_enumeration_Amass(),
                                    ansEnum_Util_concatenate_domain_names(),
                                    ),
                                await run_sequence(
                                    reverse_whois_DOMLink(),
                                    revWhois_Util_concatenate_domain_names(),
                                    ),
                            ),      
                            await run_sequence(
                                analyse_relationships_findrelationships(),
                                await run_parallelism(
                                    domain_enumeration_Waybackurls(),
                                    domain_enumeration_Assetfinder(),
                                    ),
                                domEnum_Util_concatenate_urls(),
                                #await run_parallelism(
                                aquatone_flyover(),
                                # May wait paralell urls.txt, vulnerable.txt  and domains.txt
                                ),
                            ),
                        ),
                    )




def signal_handler(sig, frame):
    print("You pressed CTRL+C!")
    print("Happy Hacking!")
    sys.exit(0)


def main():
   

    print("=======================================================================")
    print("=======================================================================")
    print("")
    print("                                 mm          mm")
    print("*@@@@*  *@@@@**                *@@@        *@@@")
    print("  @@      @@                     @@          @@   mmm")
    print("  @@      @@        m@@     m@**@@@     m@**@@@  *@@@  *@@*   *@@*")
    print("  @@@@@@@@@@       @@@@   m@@    @@   m@@    @@    @@    *@@ m@*")
    print("  !@      @!     m@* @@   @!@    @!   @!@    @!    @!      @@@")
    print("  !@      @!   m@*   @@   *!@    @!   *!@    @!    @!      !!@@")
    print("  :!      !!     !!* @!   !!!    !!   !!!    !!    !!      !!@")
    print("  :!      :!   !!*   !!   *:!    !:   *:!    !:    !:    !!* !!!")
    print("::: :   : :!:: : : : : :   : : : ! :   : : : ! : : :::  ::    :!: ")
    print("                    ::")
    print("                    ::")
    print("                            mm")
    print("*@@@***@@m                *@@@")
    print("  @@    @@                  @@")
    print("  @@    @@     m@@     m@**@@@   m@*@@@@@  @@**@m  *@@@m@@@")
    print("  @@***@mm    @@@@   m@@    @@  m@@  @@   @@@  *@@   @@* **")
    print("  @!    *@  m@* @@   @!@    @!  *!!@@@*        m@@   @!")
    print("  !!    m@m@*   @@   *!@    @!  @!           **@@m   @!")
    print("  !:    *!  !!* @!   !!!    !!  *!!!!!*        !@!   !!")
    print("  !:    !!!!*   !!   *:!    !:  !:           **!!!   !:")
    print(": !: : : :: : : ::   : : : ! :  : :!: :        :  : :::")
    print("               ::               ::     :::::  :::")
    print("               ::               :::: ::   ::::::")
    print("")
    print("=======================================================================")
    print("      OSINT Reconnaissance suite for Redteaming, Bug Bounties, etc     ")
    print("=======================================================================")

    parser = argparse.ArgumentParser(#prog='H4dd1xB4dg3r', 
                                    usage='%(prog)s [options] target_organisation', 
                                    description='Automated Bug Bounty OSINT an organisation',
                                    epilog='Happy Hacking :)',
                                    add_help=True,)

    parser.add_argument('target_organisation',
                        metavar='target_organisation', 
                        action='store', 
                        type=str, 
                        help='Provide a target organisation to OSINT')
    
    parser.add_argument('-d', 
                        metavar='domain_name', 
                        action='store', 
                        type=str, 
                        help='Provide a domain name used for intial passive recon of target - It is \"Best Practice\" to provide valid ASN - but you do you...')

    parser.add_argument('-a', 
                        metavar='asn', 
                        action='store', 
                        type=str, 
                        help='Provide a valid ASN used for intial passive recon of target - Best Practice')

    parser.add_argument('-n', 
                        metavar='project_name', 
                        action='store', 
                        type=str, 
                        help='Provide a project name used a root directory of the directory tree')

    parser.add_argument('-p', 
                        metavar='project_path', 
                        action='store', 
                        type=str, 
                        help='Provide a valid file path to store project')
    
    parser.add_argument('-s', 
                        metavar='out_of_scope_path', 
                        action='store', 
                        type=str, 
                        help='Provide a valid file path to .txt file contain out-of-scope urls, one per line')
    
    parser.add_argument('-r', 
                        metavar='recursion_count', 
                        action='store', 
                        type=int, 
                        default=3,
                        help='Provide an amount of times to recursively consildate and rerun tools on consolidated data')
     
    parser.add_argument('-c', 
                        metavar='recon_ng_custom', 
                        action='store', 
                        required=False, 
                        help='Provide a custom recon-ng resource file, see default {badger_location} ')

    
    signal.signal(signal.SIGINT, signal_handler)

    if len(sys.argv) ==	 1:
        parser.print_help()
        sys.exit(1)


    args = parser.parse_args()
    args_dict = vars(args)
    print(f"args_dict: {args_dict} and its type:{type(args_dict)}")
    current_target = Target(args_dict)
    # current_target setup

    
    # logging setup
    # 
    logging.basicConfig(filename='{Target.project_name}.log', encoding='utf-8', level=logging.DEBUG)
    log = logging.FileHandler('{path}/{project_name}.log')
    log.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s  %(levelname)s %(tool)s %(message)s')
    log.setFormatter(formatter)
    logging.debug('')
    logging.info('')
    logging.warning('')
    logging.error('')
    logging.critical('')

    # initial run

    # complete first data collection and consolidation phase checks

    # nth run

    # complete nth data collection and consolidation phase checks



if __name__ == '__main__':
    main()
