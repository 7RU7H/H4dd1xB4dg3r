#!/usr/share/python3
import os, sys, time, subprocess, logging, argparse, re
from  typing import Any, Awaitable

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


def main():
    
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
