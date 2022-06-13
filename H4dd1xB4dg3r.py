import multiprocessing as mp
import threading, os, sys, time, dataclasses, subprocess, logging, argparse
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
    out_of_scope_path: str
    project_name_path: str
    project_name: str
    badger_location: str
    toollist: list

    def __init__(self):
        organisation_root = args.organisation
        project_name_path = args.project_path 
        project_name = args.project_name
        badger_location = os.pwd()
        toollist = ['amass', 'domLink', 'assetfinder', 'waybackurls', 'theharvester', 'findrelationships']

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

    async def create_directory_forest(project_name, path):
        # All tool names
        # All found URLs
        # All custom wordlists
        # All stardardised wordlists -> transform
        # All logs
        # Domain_map
        # Domain_wordlist mapping
        os.mkdir({project_name})
        os.mkdir({project_name}/log)
        os.mkdir({project_name}/reports)
        os.mkdir({project_name}/domainmap)
        os.mkdir({project_name}/wordlists)
        for tool in self.toollist:
            tool_path = f"{path}/{project_name}/{tool}"
            os.mkdir()
        print(f"Directory forest completed a {path}")

    # TODO
    # Needs STRUCTURING by domain hierarchy!!
    def create_directory_tree_by_address(address, project_name):
        if address.Contains(".txt"):
            f = open(target_list , "r")
            address_list = f.read()
            for addr in address_list:
                os.mkdir({project_name}/domainmap/{addr}/wordlists)
        else:
            os.mkdir({project_name}/domainmap/{address}/wordlists)
        print(f"Directory structure added to {project_name}/domainmap")

         
        
    def check_out_of_scope(url):
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
                    return true
        print(f"Out-of-scope url {url} not found")
        return false


    # TODO refactor to one function, concat_domainnames, concat_urls!


    def screenshotting():

    # OSINT
    # theHarvester
    # -s for shodan
    async def osint_theHarvester(target, output_path):
        print(f"Beginning theHarvester against {target}")
        process = subprocess.Popen(["theHarvester", "-d {target} -v -n -g -r -f {output_path} --screenshot {output_path}" ], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"theHarvester OSINT against {target} complete, check {output_path}")

    # Aquistion Recon 
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

    # Acquistion Recon Utility
    async def acqRec_Util_amass_find_ans(intel_output_path, outpath_file):
        print("Getting ASN number from amass intel output")
        process = subprocess.Popen(["scripts/script_amassASN_util.sh", "{intel_output_path} {output_file}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print("Dictionary containing ASN numbers constructed")

    # cat $1 awk -F, '{print $1}' ORS=',' | sed 's/,$//' | xargs -P3 -I@ -d ',' > $2

    async def acqRec_Util_concatenate_domain_names():
        # scrap new domains
        # newdomains -> secondary_list
        # newdomains -> big_list
        # TODO refactor to one function!

    # ANS enumeration
    async def ans_enumeration_Amass(self.asnum, output_path, log_path):
        print("Beginning Amass ANS enumeration")
        for ans in self.asnum:
            print("Beginning Amass intel -ans {ans} -oA {output_path} -l {log_path}")
            process = subprocess.Popen(["amass", "intel -asn {asn} -max-dns-queries 2500 -oA {output_path} -l {log_path}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            process.wait()
            print("Amass intel -asn {asn} complete")
        print(f"Ans recon for {Target.asnum} completed")

    # ANS enumeration Utility
    async def ansEnum_Util_concatenate_domain_names():
        # scrap new domains
        # newdomains -> secondary_list
        # newdomains -> big_list
        # TODO refactor to one function!


    # Reverse whois with DomLink
    # Get an API key from WHOXY.com
    # Set that API key in a file named domLink.cfg in the same directory.

    async def reverse_whois_DOMLink(targets, output_path):
        with open(target_list , "r") as f:
            targets = f.read()
            for target in targets:
                print("Beginning reverseWHOIS with Domlink")
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

 #with open(target_list , "r") as f:
  #      urls = f.read()
   #     for target in urls:

    # Target must be a file
    async def analyse_relationships_findrelationships(project_name, badger_location, targets):
        print("Findrealtionships.py Started")
            with open(target_list , "r") as f:
                targets = f.read()
                for target in targets:
                    process = subprocess.Popen(["scripts/script_findrelationships_multi.sh", "{project_name} {badger_location} {target}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    process.wait()
                    print(f"Findrelationships.py completed analysis of {target}")
        print("Findrelationships.py completed")

    # #!/bin/bash
    # cat $3 | python3 $2/scripts/findrelationships.py 0> $1/findrelationships/findrelationships_output.txt"

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
                process = subprocess.Popen(["assetfinder", "{target} 0> {output_path}/assetfinder_output.txt", stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
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

    # Domain Enuemration Utility
    async def domEnum_Util_concatenate_urls():   
            # scrap new domains
            # newdomains -> secondary_list
            # newdomains -> big_list
            # TODO refactor to one function!
 
    async def run():
        await run_sequence(
                #scope_init_bbscope()
                    await run_parallelism(
                        osint_theHarvester()
                        # scrapping acquisition recon function(S?)
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
                                )
                            )
                        )
                    )



def main():
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
                        metavar='scope', 
                        action='store', 
                        type=str, 
                        required=True, 
                        help='Provide a valid file path to .txt file contain out-of-scope urls, one per line')


    args = parser.parse_args()

    logging.basicConfig(level=logging.{}, filename='example.log', encoding='utf-8', level=logging.DEBUG)
    log = logging.FileHandler('{project_name}.log')
    log.setLevel('')
    formatter = logging.Formatter('%(asctime)s  %(levelname)s %(tool)s %(message)s')
    log.setFormatter(formatter)
    logging.debug('')
    logging.info('')
    logging.warning('')
    logging.error('')
    logging.critical('')

    current_target = Target()
   


if __name__ == '__main__':
    main():
