#!/bin/bash
# invalid cert check
# https://gist.github.com/cgmartin/49cd0aefe836932cdc96

# https://klichx.dev/2019/11/09/f-strings-and-python-logging/

#!/bin/bash
TARGET="mysite.example.net"; 
RECIPIENT="hostmaster@mysite.example.net";
DAYS=7;
echo "checking if $TARGET expires in less than $DAYS days";
expirationdate=$(date -d "$(: | openssl s_client -connect $TARGET:443 -servername $TARGET 2>/dev/null \
                              | openssl x509 -text \
                              | grep 'Not After' \
                              |awk '{print $4,$5,$7}')" '+%s'); 
in7days=$(($(date +%s) + (86400*$DAYS)));
if [ $in7days -gt $expirationdate ]; then
    echo "KO - Certificate for $TARGET expires in less than $DAYS days, on $(date -d @$expirationdate '+%Y-%m-%d')" \
    | mail -s "Certificate expiration warning for $TARGET" $RECIPIENT ;
else
    echo "OK - Certificate expires on $expirationdate";
fi;

