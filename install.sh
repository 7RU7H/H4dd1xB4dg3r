#!/bin/bash

apt-get --assume-yes install git make gcc # for masscan

git clone https://github.com/nsonaniya2010/SubDomainizer.git
cd SubDomainizer; pip3 install -r requirements.txt
wait; cd /opt
git clone https://github.com/m8r0wn/subscraper
cd subscraper; python3 setup.py install 
wait; cd /opt
go get github.com/incogbyte/shosubgo/apishodan; cd shosubgo/; go build main.go 
wait; cd /opt
go install -v github.com/OWASP/Amass/v3/...@master
GO111MODULE=on go get -u github.com/jaeles-project/gospider
go get -u github.com/gwen001/github-subdomains
go install github.com/hakluke/hakrawler@latest
go install -v github.com/projectdiscovery/shuffledns/cmd/shuffledns@latest
git https://github.com/jhaddix/CloudBrute.git
cd CloudBrute; go build -o CloudBrute main.go
wait; cd /opt
pip3 install py-altdns==1.0.2
git clone https://github.com/devanshbatham/FavFreak
cd FavFreak; virtualenv -p python3 env
source env/bin/activate
python3 -m pip install mmh3
wait; cd /opt
# From github is then cat url.txt | python3 favfreak.py -o output
git clone https://github.com/robertdavidgraham/masscan
cd masscan; make # any other linux than ubuntu/debian add "install", Raspi requires "-j"
wait; cd /opt
apt-get install brutespray
go install -v github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest
GO111MODULE=on go get github.com/jaeles-project/jaeles
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest
bash -c "$(curl -fsSL https://raw.githubusercontent.com/osmedeus/osmedeus-base/master/install.sh)"
mkdir -p $GOPATH/src/github.com/j3ssie
git clone --depth=1 https://github.com/j3ssie/osmedeus $GOPATH/src/github.com/j3ssie/osmedeus
cd $GOPATH/src/github.com/j3ssie/osmedeus
make build
wait; cd /opt;
