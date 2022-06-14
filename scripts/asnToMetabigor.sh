#/bin/bash
# https://github.com/KingOfBugbounty/KingOfBugBountyTips
# Search ASN to metabigor and resolvers domain
echo '$1' | metabigor net --org -v | awk '{print $3}' | sed 's/[[0-9]]\+\.//g' | xargs -I@ sh -c 'prips @ | hakrevdns | anew'
