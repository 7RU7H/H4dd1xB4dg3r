#!/bin/bash

username
password
domain
port 
workstation
smbhash
userlist
passlist

nmap -p $port --script smb-enum-users $target --script-args smbuser=$username,smbpass=$password,smbdomain=$domain 
nmap -p $port --script smb-enum-users $target --script-args smbuser=$username,smbhash=$smbhash,smbdomain=$domain
nmap --script smb-enum-users.nse --script-args smbusername=$username,smbpass=$password,smbdomain=$workstation -p$port $IP
nmap --script smb-enum-users.nse --script-args smbusername=$username,smbhash=$smbhash,smbdomain=$domain -p$port $IP
echo "Enumerating Groups"
echo
nmap -p $port --script smb-enum-groups $target --script-args smbuser=$username,smbpass=$password,smbdomain=$domain 
nmap -p $port --script smb-enum-groups $target --script-args smbuser=$username,smbhash=$smbhash,smbdomain=$domain
echo "Enumeration Shares"
echo
nmap -p $port --script smb-enum-shares $target --script-args smbuser=$username,smbpass=$password,smbdomain=$domain 
nmap -p $port --script smb-enum-shares $target --script-args smbuser=$username,smbpass=$smbhash,smbdomain=$domain
echo "OS Discovery"
echo
nmap -p $port --script smb-os-discovery $target
echo "Exposing SMB Vulnerabilities on Windows"
echo 
nmap -p $port --script smb-vuln-ms06-025 $target
nmap -p $port --script smb-vuln-ms07-029 $target
nmap -p $port --script smb-vuln-ms08-067 $target
nmap -p $port --script smb-vuln-ms10-054 $target
nmap -p $port --script smb-vuln-ms10-061 $target
nmap -p $port --script smb-vuln-ms17-010 $target
echo "Bruteforcing smblogin"
echo
nmap –p $port --script smb-brute –script-args userdb=$userlist,passdb=$passlist $target
