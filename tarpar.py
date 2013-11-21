#! /usr/bin/env python

import argparse
from datetime import date
import subprocess
import socket

parser = argparse.ArgumentParser(description='Backup internal disk.')
parser.add_argument('destination', help='backup destination path')
args = parser.parse_args()

sources = [
    "/Applications", 
    "/Library",
    "/System",
    "/Users",
    "/opt",
    "/private/etc",
    "/usr/local"]

today = date.today().isoformat()
hostname = socket.gethostname().split('.')[0]
destination = hostname + "_" + today

### 
# create backup using tar

bupcmd = "caffeinate -s gtar -cvW -f " + args.destination + "/" + destination + ".tar " + " ".join(sources) + " 2> " + args.destination +  "/" + destination + ".err"

print(bupcmd)
subprocess.call(bupcmd, shell = True)

###
# create parchive

parcmd = "caffeinate -s par2 c -n1 -r5 -vv " + args.destination + "/" + destination + ".tar && par2 v -vv " + args.destination + "/" + destination + ".tar"

print(parcmd)
subprocess.call(parcmd, shell = True)



