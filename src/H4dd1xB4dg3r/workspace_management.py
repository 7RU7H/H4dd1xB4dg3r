#!/usr/share/python3

# poss bad idea : flush used memory to init.

toollist = ['reconftw', 'osmedeus', 'nuclei', 'amass', 'domLink', 'assetfinder', 'waybackurls', 'shuffleDNS', 'gospider', 'hakrawler', 'subdomainizer', 'httprobe', 'dnmasscan', 'nmap', 'masscan', 'brutespray', 'nikto', 'wcvs', 'favfreak','techstack', 'gron', 'ssrfmap', 'sqlmap', 'subdomainizer', 'shuffleDNS', 'domlink', 'theharvester', 'reconng', 'findrelationships'];
# for reference update opt_function_name tool here:
#opt_toollist = ['wpscan'];


def create_directory_forest(project_name):
    os.mkdir({project_name})
    os.mkdir({project_name}/log)
    os.mkdir({project_name}/reports)
    os.mkdir({project_name}/domainmap)
    os.mkdir({project_name}/wordlists)
    for tool in toollist:
        os.mkdir({project_name}/tool)

    process = subprocess.Popen(["recon-cli", "-w {project_name}/reconng/initial"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Workspace directory structure for {project_name} complete.")

def create_directory_addition_tools(toolname):
    os.mkdir({project_name}/{toolname})
    print(f"Optional tool directory add at: {project_name}/{toolname}")

def create_addition_reconng_workspace(project_name, addition):
    process = subprocess.Popen(["recon-cli", "-w {project_name}/reconng/{addition}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"Recon-ng Workspace directory structure for {project_name}/reconng/{addition} complete.")

def populate_initial_forest(project_name):
    process = subprocess.Popen(["curl", "https://datatracker.ietf.org/doc/html/rfc1866 -o {project_name}/wordlists/rfc1866.html"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    process.wait()
    print(f"cUrl-ed rfc1866  for uniq wordlist bashing outputed to {project_name}/wordlists/rfc1866.html")


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



