#!/usr/bin/python
import multiprocessing as mp
import threading, os, sys, time, dataclasses, subprocess, logging, argparse, re
# import workspace_management internalise it in the class

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
    project_name_file_path: str
    project_name: str
    badger_location: str
    toollist: list
    domain_name_file_path: str
    recon_ng_custom_resource_file_exists: bool
    recon_ng_custom_file_checks: bool
    recon_ng_resource_file_path: str


    def __init__(self):
        self.organisation_root = args.organisation
        self.domain_root = args.domain_name
        self.toollist = ['amass', 'aquatone', 'domLink', 'assetfinder', 'waybackurls', 'theHarvester', 'findrelationships', 'recon-ng']
        self.recon_ng_custom_resource_file_exists = False
        self.recon_ng_custom_file_checks = False

        if path.exists({args.project_path}):
            self.project_name_file_path = args.project_path
        else:
            print(f"Error Invalid project path: {args.project_path}")
            exit(1)
        if path.exists({args.project_name}): 
            print(f"Error project name already exists: {args.project_name}")
            exit(1)
        else:
            self.project_name = args.project_name

        self.domain_names_list += args.domain_name
        self.out_of_scope_path = args.out_of_scope_path
        self.recursive_osint_count = args.recursive_osint_count
        self.badger_location = os.Exec('pwd')
        
        if arg.recon_ng_custom_resource_file != None:
            if path.isfile({arg.recon_ng_custom_resource_file}):
                assign_custom_reconng_resource_file()
            if self.recon_ng_custom_file_checks != True:
                print(f"Error Invalid recon_ng custom resource file: {arg.recon_ng_custom_resource_file}")
                exit(1)
            else:
                # if custom recon-ng resource file path path set bool and path  else default resource file 
                assign_custom_reconng_resource_file()
        else:
            self.recon_ng_custom_resource_file = f"{self.badger_location}/recon-ng/recon-ng-default-resource-file.txt"

        # init cli checks

    
 
    def check_custom_recon_ng_file(filepath): #TODO
        extension_test = False
        if filepath.contains(".txt"):
            extension_test = True

    def assign_custom_reconng_resource_file():
            self.recon_ng_resource_file_path = arg.recon_ng_custom_resource_file 
            self.recon_ng_custom_resource_file = True
            self.recon_ng_custom_file_checks = check_custom_recon_ng_file() # TODO
            print(f"custom resource file accepted and will be moved to {self.project_path}/recon-ng/")


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

    # TODO script check and called tool checks seperate
    # Script check and 
    async def check_valid_install():
        install_check_theHarvester = subprocess.Popen(["theHarvester", "-h"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        install_check_theHarvester = subprocess.Popen(["recon-cli", "-h"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        install_check_amass = subprocess.Popen(["amass", "-h"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        install_check_domlink = subprocess.Popen(["python /opt/DomLink/domLink.py","-h" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        install_check_findrelationships = subprocess.Popen(["scripts/script_findrelationships_multi.sh", ""], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        install_check_assetfinder = subprocess.Popen(["assetfinder", "-h"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        install_check_waybackurl = subprocess.Popen(["scripts/script_waybackurl.sh", ""], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()

    def create_directory_forest(project_name, path):
        os.mkdir({path}/{project_name})
        os.mkdir({path}/{project_name}/log)
        os.mkdir({path}/{project_name}/reports)
        os.mkdir({path}/{project_name}/domainmap)
        os.mkdir({path}/{project_name}/wordlists)
        os.mkdir({path}/{project_name}/wordlists/scrappings)
        os.mkdir({path}/{project_name}/wordlists/custom)
        os.mkdir({path}/{project_name}/wordlists/utility)
        for tool in self.toollist:
            tool_path = f"{path}/{project_name}/{tool}"
            os.mkdir(tool_path)
        if recon_ng_custom_resource_file_exists && recon_ng_custom_resource_file_exists:
            os.rename("{self.recon_ng_resource_file_path}", "{self.badger_location}/recon-ng/recon-ng-default-resource-file.txt") 
        print(f"Directory forest completed a {path}")

    # TODO
    # Needs STRUCTURING by domain hierarchy!!
    def create_directory_tree_by_address(address, project_name):
        if address.Contains(".txt"):
            f = open(target_list , "r")
            address_list = f.read()
            for addr in address_list:
                os.mkdir({path}/{project_name}/domainmap/{addr}/wordlists)
        else:
            os.mkdir({path}/{project_name}/domainmap/{address}/wordlists)
        print(f"Directory structure added to {path}/{project_name}/domainmap")

         
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

    async def trim_excess_from_domain_name(url):
        rm_proto_and_dir = str(re.findall(r':\/\/(.[^/]+)', url))
        unlist = rm_proto_and_dir[0]
        dots_split = re.split('[.]', rm_proto_and_dir.strip())
        tld = str(re.sub(r'[^a-z-A-Z0-9 ]', "", dots_split[-1]))
        result = f"{str(dots_split[-2])}.{tld}"
        return result

    async def check_uniq_domain_name(domain_name):
        if self.non_uniq_domain_names.contains(domain_name):
            add_new_domain_name()
        # else: check the queue and remove any that QUEUE 
                
    async def add_new_domain_name():
        with open(self.domain_names_file_path, "a") as f:
            f.write(domain_name)
            self.domain_names_historic += domain_name
            print(f"Found a new domain name: {domain_name}")

    
    # From each util_concatenation function
    # a instance of gurl will take one file of a list of filenames passed into the util function and perform 
    # faster than grep greppage of urls and then formats and appends them if fileexists or create the file if it does not
    # It takes -u {urltype} for formating to, -i {input_file} -o {output_file} {-a}
    async def gurl_url_list_concatenation(url_format_type, input_path, output_path, append_flag):
        print(f"Beginning gurl_url_list_concatenation {} with formatting options {url_format_type}")
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

    # Acquistion Recon 
    async def acquistion_recon_wordlist_generation():
        #scrap crunchbase, wiki, google
        # GO GO GO

    async def acquisition_recon_Amass_ORG(Target.organisation_root, output_path, log_path):
        print("Beginning Amass intel -org")
        process = subprocess.Popen(["amass", "intel -src -org {Target.organisation_root} -max-dns-queries 2500 -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print("Amass intel -src -org complete")

    async def acquisition_recon_Amass_CIDR(Target.cidr_range, output_path, log_path):
        print("Beginning Amass intel -src -cidr {}")
        process = subprocess.Popen(["amass", "intel -src -cidr {Target.cidr_range} -max-dns-queries 2500 -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
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
    async def ans_enumeration_Amass(self.asnum, output_path, log_path):
        print("Beginning Amass ANS enumeration")
        for ans in self.asnum:
            print("Beginning Amass intel -ans {ans} -oA {output_path} -l {log_path}")
            process = subprocess.Popen(["amass", "intel -asn {asn} -max-dns-queries 2500 -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            process.wait()
            print("Amass intel -asn {asn} complete")
        print(f"Ans recon for {self.asnum} completed")

    # ANS enumeration Utility
    async def ansEnum_Util_concatenate_domain_names():
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
    async def revWhois_Util_concatenate_domain_names():
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
    async def domEnum_Util_concatenate_urls():   
            # scrap new domains
            # newdomains -> secondary_list
            # newdomains -> big_list
            # TODO refactor to one function!

    # Domain FLyerover with screenshots
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
                        osint_theHarvester()
                        osint_recon_ng()
                        # scrapping acquisition recon function(S?)
                        # metabigor!!
                        await run_sequence(
                            acquisition_recon_Amass_ORG()
                            acquisition_recon_Amass_CIDR()
                            await run_parallelism(
                                acqRec_Util_amass_find_ans()
                                acqRec_Util_concatenate_domain_names()
                             )
                            await run_parallelism(
                                await run_sequence(
                                    ans_enumeration_Amass()
                                    ansEnum_Util_concatenate_domain_names()
                                    )
                                await run_sequence(
                                    reverse_whois_DOMLink()
                                    revWhois_Util_concatenate_domain_names()
                                    )
                            )      
                            await run_sequence(
                                analyse_relationships_findrelationships()
                                await run_parallelism(
                                    domain_enumeration_Waybackurls()
                                    domain_enumeration_Assetfinder()
                                    )
                                domEnum_Util_concatenate_urls()
                                #await run_parallelism(
                                aquatone_flyover()
                                # May wait paralell urls.txt, vulnerable.txt  and domains.txt
                                #    )
                                )
                            )
                        )
                    )



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
    print(": !: : : :: : : : :   : : : ! :  : :!: :        :  : :::")
    print("               ::               ::     :::::  :::")
    print("               ::               :::: ::   ::::::")
    print("")
    print("=======================================================================")
    print("OSINT Reconnaissance suite for Redteaming, Bug Bounties, etc"
    print("=======================================================================")

    parser = argparse.ArgumentParser(prog='H4dd1xB4dg3r', 
                                    usage'%(prog)s [options] target', 
                                    add_help=True, 
                                    description='Automated Bug Bounty OSINT an organisation',
                                    epilog='Happy Hacking :)')

    parser.add_argument('target_organisation',
                        metavar='organisation', 
                        action='store', 
                        type=str, 
                        required=True, 
                        help='Provide a target organisation to OSINT')
    
    parser.add_argument('-d', 
                        metavar='domain_name', 
                        action='store', 
                        type=str, 
                        required=True, 
                        help='Provide a domain name used as intial passive recon target')

    parser.add_argument('-n', 
                        metavar='project_name', 
                        action='store', 
                        type=str, 
                        required=True, 
                        help='Provide a project name used a root directory of the directory tree')

    parser.add_argument('-p', 
                        metavar='project_path', 
                        action='store', 
                        type=str, 
                        required=True, 
                        help='Provide a valid file path to store project')
    
    parser.add_argument('-s', 
                        metavar='out_of_scope_path', 
                        action='store', 
                        type=str, 
                        required=False, 
                        help='Provide a valid file path to .txt file contain out-of-scope urls, one per line')
    
    parser.add_argument('-r', 
                        metavar='recursive_osint_count', 
                        action='store', 
                        type=int, 
                        required=False, 
                        default=3,
                        help='Provide an amount of times to recursively consildate and rerun tools on consolidated data')
     
    parser.add_argument('--recon-ng-custom', 
                        metavar='recon_ng_custom_resource_file', 
                        action='store', 
                        type=str, 
                        required=False, 
                        help='Provide a custom recon-ng resource file, see default {badger_location} ')


    




    args = parser.parse_args()

    current_target = Target
    # current_target setup

    
    # logging setup

    logging.basicConfig(level=logging.{}, filename='example.log', encoding='utf-8', level=logging.DEBUG)
    log = logging.FileHandler('{path}/{project_name}.log')
    log.setLevel('')
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
