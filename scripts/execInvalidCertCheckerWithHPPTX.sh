#!/bin/bash
# From https://github.com/KingOfBugbounty/KingOfBugBountyTips
# Runs the scripts/invalidCertChecker.sh and  
bash invalidCertChecker.sh @ 2> /dev/null | grep "EXPIRED" | awk '/domain/{print $5}' | httpx
