#!/usr/share/python3
import os, sys, time, subprocess, logging, argparse, re
from  typing import Any, Awaitable
from dataclasses import  dataclass
# import workspace_management internalise it in the class

# slots break in multiple inheritance AVOID, 20% efficiency over no slot dict
@dataclass(slots=True)
class Target:
    host_ip: str
    domain_name: str
    subdomain_list: list
    protocol_port_dict: dict

    def __init__(self):
        self.host_ip = args.host




async def run_sequence(*functions: Awaitable[Any]) -> None:
    for function in functions:
        await function

async def run_parallelism(*functions: Awaitable[Any]) -> None:
    await asyncio.gather(*functions)

# Grep http and https, into a map to cycle through grep {nmap_sc_sv_file} 'http \| https'


# gospider
async def spider_target_Gospider(target):
        blacklistStr = f"jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt"
        print(f"Running Gospider against {target} with {blacklistStr}")      
        process = subprocess.Popen(["gospider", "-s -a --subs --sitemap --robots --js {blacklistStr} -o gospider-{target} "], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        process.wait()
        print(f"Completed Gospider against {siteStr} with {blacklistStr}")


async def bulk_gospider(targets_list):
    for target in targets_list:
        spider_target_Gospider(target)

        
# Handle urls into a map

# nuclei
async def subdomain_takeover_Nuclei(target):
    if target.contains(".txt"):
        targetstr = f"-list {target}"
    else:
        targetstr = f"-u {target}"        
    print(f"Running Nuclei with the target flag and arguments set to: {targetStr}")   
    process = subprocess.Popen(["nuclei", "{targetStr} -me nuclei"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Completed Nuclei against {targetStr}")

async def bulk_nuclei():
    for target in targets_list:
        subdomain_takeover_Nuclei(target)

# nikto
async def web_scanning_Nikto(target):
    print(f"Starting Nikto scanning on {target}")
    process = subprocess.Popen(["nikto", "-h {target} -C all -o nikto/{target}.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Finished Nikto scanning on {target}") 

async def bulk_nikto(targets_list):
    for target in targets_list:
        web_scanning_nikto(target)


# feroxbuster


# -d domain 
# -s subdomain
# -h host
# -o directory name
# -ssl enable https ssl flags

def main():
    
    parser = argparse.ArgumentParser(#prog='WebAppRecon.py',
                                    usage='%(prog)s [options]',
                                    description='Automated Web Application Recon',
                                    epilog='Happy Hacking :)',
                                    add_help=True,)

    parser.add_argument('-d',
                        metavar='domain',
                        action='store',
                        type=str,
                        required=False,
                        help='Provide domain name')
    
    parser.add_argument('-h',
                        metavar='host',
                        action='store',
                        type=str,
                        required=True,
                        help='Provide host IP')

    parser.add_argument('-o',
                        metavar='output_path',
                        action='store',
                        type=str,
                        required=True,
                        help='Provide output directory to create directories for each tool\'s output')

    parser.add_argument('-p',
                        metavar='ports_user_string',
                        action='store',
                        type=str,
                        required=False,
                        help='Provide a list of ports demlimitered with commas')

    parser.add_argument('-s',
                        metavar='subdomain_list',
                        action='store',
                        type=str,
                        required=False,
                        help='Provide subdomain domain names, if lists ns0, ns1 this script will concatenate full urls - for effiency do not provide dots, but will remove dots just incase')

    parser.add_argument('-ssl',
                        metavar='enable_ssl',
                        action='store',
                        type=bool,
                        required=False,
                        help='Enable ssl')
    
    args = parser.parse_args()    

    run_sequence(
            create_directories()
            targets_list = create_urls()
            bulk_gospider(targets_list)
            run_parallelism(
                bulk_nuclei(targets_list)
                bulk_nikto(targets_list)
            )
            run parallelism(
            
            )
    os.exit(0)



if __name__ == '__main__':
    main()
