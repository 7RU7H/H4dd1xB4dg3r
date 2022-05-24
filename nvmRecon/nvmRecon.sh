#!/bin/bash


function lootAnonymousFTP () 
{
	FTPANONCHECK=$(grep nmap/ -r -e  "Anonymous FTP login allowed (FTP code 230)"|  wc -l)
	if [$FTPANONCHECK > 0];
	then
		wget -r ftp://Anonymous:@$IP/
		wait;
	       	echo "Completed looting the Anonymous FTP login" && echo "Completed looting the Anonymous FTP login!" >> output.log
		mv $IP ftp-anon-loot
	       	echo
	else
		echo "No Anonymous login allowed skipping looting phase"
		echo
	fi
	
	return 1;
}

function ikeEnumeration ()
{
	mkdir ike
	ike-scan $IP # ike/  outputtricks?
	return 1;
}

function snmpEnumeration () 
{
	echo "Beginning snmpwalk scan" && echo "Beginning snmpwalk scan" >> output.log 
	echo
	snmpwalk -c public -v2c $IP -L snmpwalk/snmpwalk-$IP.log
	wait
	echo "Completed snmpwalk scan" && echo "Completed snmpwalk scan" >> output.log
	echo
	#snmp-check | grep ".1*2" needs to be a 7 or 9  # indicte routing to vm
	return 1;
}

function smbEnumeration ()
{
	# smbmap to find exposed shares 	
	# enum4linux - General enumeration - anonymous session
	cd smbmap;
	SMBMAPOUT=$(python3 smbmap.y -H $IP 1> smbmap/guestSMB.txt) # Show read, no access write
	wait
	cd ../
	EFLBASIC=$(enum4linux -a 1> enum4linux/all.txt)
	wait
	read ENUM4LINUX_RIDRANGE -p "Enter a rid range for Enum4Linux"
	EFLEXTS=$(enum4linux -U -S -P -G -o -d -r -K $ENUM4LINUX_RIDRANGE 1> enum4linux/ridranged.txt )
	#./nmapSMB.sh
        return 1;
}

function nucleiRecon ()
{	
	case $@ in
		1) nuclei http://$IP:$PORT -me $Proj-http; wait; echo "Nuclei Scan Completed on $PORT" && echo "Nuclei Scan Completed on $PORT" >> output.log; break;;
		2) nuclei https://$IP:$PORT -me $Proj-https; wait; echo "Nuclei Scan Completed on $PORT" && echo "Nuclei Scan Completed on $PORT" >> output.log; break;;
		3) nuclei http://$IP:$PORT -me $Proj-http; wait; nuclei https://$IP:$PORT -me $Proj-https; wait; echo "Nuclei Scans Completed on $PORT and $PORT" && echo "Nuclei Scans Completed on $PORT and $PORT" >> output.log; break;;
	     	*) echo "Argument passed to nucleiRecon a non 1-3 int" && echo "Argument passed to nucleiRecon a non 1-3 int" >> output.log; return 0;;
	esac
	echo
	return 1;
}

FRAMEART="================================================================"

read -r -p "Enter a project name: " PROJ
echo
read -r -p "Enter and IP address: " IP
echo
STARTTIME=$(date)
while true; do
        read -r -p "Do you any of these tools, should a required within tool directory: " TOOLRSP
        case $TOOLRSP in
                [Yy]* ) installGitTools; wait; echo "Completed getting all the tools"; echo; break ;;
                [Nn]* ) break;;
                * ) echo "Please answer Y or N.";;
        esac
done
echo "Conducting Ping test.." 
echo
PINGOUT=$(ping -W 30 -c 1 $IP) # check output if -Pn needed; if just exit - # TODO ttl for os detection
wait
echo "Ping test complete!"
echo
echo $PINGOUT > pingtest.log
PINGRECV=$(cut pingtest.log -d ' ' -f 40)
if ["$PINGRECV" != "3"]
then
        echo "Ping test recieved $PINGRECV packets"
        echo
        #UPCHECK=isTargetUp
        #if UPCHECK ! 0
        #then
                NMOPTFLAG="-Pn "
        #else
               # echo "Target is not avaliable"
               # exit
        #fi
else
        NMOPTFLAG=""
fi
echo "Optional nmap flag set to $NMOPTFLAG"  
echo
mkdir -p $PROJ/tools; cd $PROJ
mkdir tools/{nmap, nikto, dirb, gobuster, brutespray, smbmap, enum4linux, nuclei}
touch output.log && touch nmap/allTheNSEScripts.txt &&  touch nikto/foundbyNikto.txt;
cd -;mv pingtest.log $PROJ/pingtest.log; cd -;
echo "Project name: $PROJ IP: $IP Time: $STARTTIME" && echo "Project name: $PROJ IP: $IP Time: $STARTTIME" >> output.log
echo
echo
echo "Directory and file tree built" && echo "Directory and file tree built" >> output.log
echo
echo "Optional nmap flag set to $NMOPTFLAG" >> output.log
echo "Quickly scanning to allow for research and manual enumeration.." && echo "Quickly scanning to allow for research and manual enumeration.." >> output.log
echo
# TODO a -sT -sU versions for each if required, when refactored in to functions, $-O optional OS scanning 
echo $FRAMEART && echo $FRAMEART >> output.log 
echo
nmap $NMOPTFLAG -oA nmap/Basic -F $IP
wait
echo $FRAMEART && echo $FRAMEART >> output.log 
cat nmap/Basic.nmap >> output.log
echo $FRAMEART && echo $FRAMEART >> output.log 
echo
echo "Basic scan is complete" && echo "Basic scan is complete" >> output.log
echo 
echo "Building web port lists for vulnerablity scanners.."
echo
#
# Consider logging per port
#
# grep for http and scan with nikto and brute force directories
# TODO UNIQ port numbers uniq requires file
# WEBFILE
# WEBSERVICES
WEBCOUNT=$(grep nmap/Basic.nmap -e "/tcp \+open \+http" | wc -l)
WEBSTR=$(grep nmap/Basic.nmap -e "/tcp \+open \+http" | tr -d '[a-zA-Z]/_.:' | cut -d ' ' -f 1 | tr -s '\n' ', ')
WEBLIST=${NMWEBSTR::-1}
WEBSPACED=$(echo $WEBSTR | tr -s ', ' ' ')
echo $FRAMEART && echo $FRAMEART >> output.log 
echo
echo "Web ports found and lists made: $WEBLIST $WEBSPACED" && echo "Web ports found and lists made: $WEBLIST $WEBSPACED" >> output.log
echo
echo "Starting extensive nmap scanning.." && echo "Starting extensive nmap scanning.." >> output.log
echo
nmap $NMOPTFLAG -sC -sV -O -oA nmap/Extensive -p- $IP
wait
echo $FRAMEART && echo $FRAMEART >> output.log 
cat nmap/Extensive.nmap >> output.log
echo $FRAMEART && echo $FRAMEART >> output.log 
echo "Building more extensive port listings for further scans, research and documentation" && echo "Building more extensive port listings for further scans, research and documentation" >> output.log
echo
# TODO 
# file for uniq to ensure uniq port numbers!
#grep for services listed in lines, tr, cut, and awk your way to success
#TCPSERVICE=$(grep nmap/Extensive.nmap -e "/tcp \+open" |  
# Protocol https/http or both flag for nuclei
TCPCOUNT=$(grep nmap/Extensive.nmap -e "/tcp \+open" | wc -l)
TCPSTR=$(grep nmap/Extensive.nmap -e "/tcp \+open" | tr -d '[a-zA-Z]/._:' | cut -d ' ' -f 1 > sourcable/tcports
TCPCOMMA=$(sort sourcable/tcpports | uniq | tr -s '\n' ', ')
TCPLIST=${TCPCOMMA::-1}
#UDPSERVICE=$()
UDPCOUNT=$(grep nmap/Extensive.nmap -e "/udp \+open" | wc -l) 
UDPSTR=$(grep nmap/Extensive.nmap -e "/udp \+open" | tr -d '[a-zA-Z]/._:' | cut -d ' ' -f 1 > sourcable/udpports
UDPCOMMA=$(sort sourcable/udpports | uniq | tr -s '\n' ', ')
UDPLIST=${UDPCOMMA::-1}
PORTLIST=$TCPCOMMA$UDPLIST
echo "Completed Extensive list build phase" && echo "Completed Extensive list build phase" >> output.log 
echo
echo $FRAMEART && echo $FRAMEART >> output.log 
echo
echo "TCP ports found and lists made: $TCPLIST $TCPSPACED" && echo "TCP ports found and lists made: $TCPLIST $TCPSPACED" >> output.log
echo
echo "UDP ports found and lists made: $UDPLIST $UDPSPACED" && echo "UDP ports found and lists made: $UDPLIST $UDPSPACED" >> output.log
echo
echo "Checking for Anonymous FTP logon lootables" && echo "Checking for Anonymous FTP logon lootables" >> output.log
lootAnonymousFTP
wait
echo
echo "Starting Brutespray on all services" && echo "Starting Brutespray on all services"
echo
brutespray --file nmap/Extensive.gnmap -o brutespray/ &
echo "Starting Nuclei scanning" &&  echo "Sttarting Nuclei scanning" >> output.log
echo
nucleiRecon
echo 
echo "Starting Nikto scanning" && "Starting Nikto scanning" >> output.log
# TODO vhost flag
for PORT in $WEBSPACED; do
        nikto -h $IP -port $PORT -output nikto/port-$PORT.txt -C all
        wait
done
echo "All Nikto scanning is complete." && echo "All Nikto scanning is complete."
echo
echo $FRAMEART && echo $FRAMEART >> output.log 
echo 
echo "Checking for interesting directories in Nikto output for dirb and gobuster" && echo "Checking for interesting directories in Nikto output for dirb and gobuster" >> output.log
echo
# Would like all filename where each output so for loop and no -r
NKFLIST=$(ls nikto/)
for FILE in $NKFLIST; do
        grep nikto/$FILE -e "This might be interesting..." >> nikto/foundbyNikto.txt
        grep nikto/$FILE -e "Admin login page/section found" >> nikto/foundbyNikto.txt
        # TODO add more
done

#dirb & gobuster for -x

for WEBPORT in $WEBSPACED; do
        dirb http://$IP:$WEBPORT -o dirb/port-$WEBPORT -w -i #finetune error requires!
        wait
	DIRBFTERROR=$(grep dirb/port-$WEBPORT "Try using FineTunning")
	if DIRBFTERROR == "    (Try using FineTunning: '-f')"
	then
		dirb http://$IP:$WEBPORT -o dirb/port-$WEBPORT -w -i -f 
	fi
	echo "http://$IP:$WEBPORT brute forced" && echo "http://$IP:$WEBPORT brute forced" >> output.log
done

#make a uniq port wp url list
#WPENUM=$(grep -r dirb/ -e "wp-" | uniq) 
if WPBOOL == 1
	echo "Starting wpscans" && echo "Starting wpscans" >> output.log
	wpscanEnum $WPURLIST
	wait;
fi


# TODO ideas
# curling and grepping for versions
# curling for HTTP method types for bruteforce login pages
echo "Beginning NSE scripts enumeration"
echo
echo $FRAMEART && echo $FRAMEART >> output.log 
echo 
# TODO design issues with background and multiple processes not destorying the terminal

#$SERVICE and port storage issue

LIST=$(ls /usr/share/nmap/scripts/ | grep "$SERVICE")
FILE=$(echo $LIST >> allTheNSEScripts)
FILE=$(cat scriptsReq.txt)

SERVICEPORT=
for SCRIPT in $FILE; do
        nmap --script $SCRIPT -oA nmap/$SCRIPT -p $SERVICEPORT $IP
        wait
done



#if grep "snmp"
snmpEnumeration



#if 450 5000 port
ikeEnumeration

echo "Starting nmap discovery script enumeration" && echo "Starting nmap discovery script enumeration" >> output.log
echo
nmap $NMOPTFLAG --script discovery -oA nmap/Discovery -p $REVISEDPL $IP &
wait
echo "Nmap discovery script enumeration complete" && echo "Starting nmap discovery script complete" >> output.log
echo
echo "Starting nmap vuln script enumeration" && echo "Starting nmap vuln script enumeration" >> output.log
echo
nmap $NMOPTFLAG --script vuln -oA nmap/Vuln -p $REVISEDPL $IP &
wait
echo "Nmap vuln script enumeration complete" && echo "Starting nmap vuln script complete" >> output.log
echo

#TODO add echo >> outputlog


# if grep smbi 
# IF port 137-9 or 445 are SMB
echo "REMINDER enum4linux & smbmap enumeration is account based, only basic scan performed"
echo 
#smbmap
if [$SMBFOUND == 1]
then 
	smbEnumeration
	wait	
	echo "SMB share enumeration complete" && echo "SMB share enumeration complete" >> output.log
       	echo	
else
	echo "SMB share enumeration skipped" && echo "SMB share enumeration skipped" >> output.log





#Completion clean up
wait
echo "All tasks have been completed"
exit;



GBEXTCMPRD=".7z,.gz,.jar,zip"
GBDIR="dir"
GBVHOST="vhost"


#Directory igger
gobuster -u 
TARGDIR=$

http://
https://

$IP

/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
/usr/share/wordlists/dirb/big.txt


# smart extension choice
function gobusterSmartExtensions () 
{
        grep "Apache"


        return 1;
}
-x
txt
js
php
asp

