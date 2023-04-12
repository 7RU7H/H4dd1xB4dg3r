#!/bin/bash

apt-get update
apt-get upgrade
apt-get dist-upgrade
apt install python3
apt install golang-go
apt-get --assume-yes install git make gcc # for masscan
apt-get install amass brutespray
apt install theharvester recon-ng wpscan
cd /opt
bash -c "$(curl -fsSL https://raw.githubusercontent.com/osmedeus/osmedeus-base/master/install.sh)"
wait;
git clone https://github.com/nsonaniya2010/SubDomainizer.git
cd SubDomainizer; pip3 install -r requirements.txt; 
wait; cd /opt
git clone https://github.com/m8r0wn/subscraper
cd subscraper; python3 setup.py install 
wait; cd /opt
git clone https://github.com/vysecurity/DomLink.git

git clone https://github.com/robertdavidgraham/masscan
cd masscan; make # any other linux than ubuntu/debian add "install", Raspi requires "-j"
wait; cd /opt
git https://github.com/jhaddix/CloudBrute.git
cd CloudBrute; go build -o CloudBrute main.go
wait; cd /opt
git clone https://github.com/swisskyrepo/SSRFmap
cd SSRFmap/; pip3 install -r requirements.txt; 
wait; cd /opt
git clone https://github.com/six2dez/reconftw
/reconftw/install.sh
wait;


GO111MODULE=on go install github.com/jaeles-project/gospider
go install github.com/gwen001/github-subdomains 
go install github.com/hakluke/hakrawler@latest
go install -v github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest
go install github.com/tomnomnom/unfurl@latest
go install github.com/tomnomnom/concurl@latest
go install github.com/tomnomnom/waybackurls@latest
go install -v github.com/Hackmanit/Web-Cache-Vulnerability-Scanner@latest
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest


#go get github.com/incogbyte/shosubgo/apishodan; cd shosubgo/; go build main.go 
#wait; cd /opt

pip3 install py-altdns==1.0.2

git clone https://github.com/devanshbatham/FavFreak
cd FavFreak; virtualenv -p python3 env
source env/bin/activate
python3 -m pip install mmh3
wait; cd /opt

npm install -g is-website-vulnerable

#TODO 
#recon-ng setup
#recon-cli -C 
# https://tryhackme.com/room/redteamrecon



# Old but not forgetten
# go install github.com/tomnomnom/meg@latest
# git clone https://github.com/tomnomnom/gf.git
#

