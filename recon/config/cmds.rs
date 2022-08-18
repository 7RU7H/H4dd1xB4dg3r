//A rust way for this:
//hostuptest=$(nmap -sn $IP | grep "host up" | awk '{print $7 $8}' | tr -d ')')

const ping_cmd : str = "ping -c 3 ";
const masscan_cmd : &str = "sudo masscan -p0-65535 -oG masscan/masscan.log";
const masscan_rate_flag : &str "--rate=" 
const masscan_interface : &str "-e ";

const nmap_base_cmd : &str = "sudo nmap ";
const nmap_pn_flag : &str = "-Pn ";
const nmap_ext_flags : &str = "-sC -sV -oA nmap/Extensive -p- ";
const nmap_script_disc_flags : &str = "--script discovery -oA nmap/Discovery -p- ";
const nmap_script_vuln_flags : &str = "--script vuln -oA nmap/Vuln -p- ";
const nmap_su_flags : &str = "-sU -p- nmap/UDP $nmaprate -p-";

# ssl for nikto, https http, ports
gospider -d 0 -s "$URL" -c 5 -t 100 -d 5 --blacklist jpg,jpeg,gif,css,tif,tiff,png,ttf,woff,woff2,ico,pdf,svg,txt -o gospider
nikto -h $IP -port $PORT -output nikto/port-$PORT.txt 
nuclei -u $PROTO://$DOMAIN -me nuclei


// snmpwalk
const snmpwalk_base_cmd : &str "snmpwalk -c public ";
const snmpwalk_v1_flag : &str = "-v1 ";
const snmpwalk_v2c_flag : &str = "-v2c ";

// Content Discovery


feroxbuster -u $URL -w $WORDLIST --auto-bail -o feroxbuster/$project -x # space delimited extensions



//JS parsing

python3 xnLinkFinder.py -i $URL -o xnLinkFinder/$URL

//SMB
enum4linux -a $IP | tee -a $file

// Utility
const tee_auth_cmd : &str = "sudo tee -a ";
const tee_nonauth_cmd : &str = "tee -a ";
const base_pipe :  &str = " | ";
const base_and : & str = " & ";
