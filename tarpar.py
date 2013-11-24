#! /usr/bin/env python

import argparse
from datetime import date
import subprocess
import socket

parser = argparse.ArgumentParser(description='Create a tar and par2 archive of selected folders of the internal disk. The name of the archive is derived from the hostname and current date.')
parser.add_argument('--tryonly', action='store_true', help='print but do not execute backup commands')
parser.add_argument('destination', help='path to external backup destination, e.g. /Volumes/bup1')
args = parser.parse_args()

# folders to backup
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

bupcmd = "gtar -cvW -f " + args.destination + "/" + destination + ".tar " + " ".join(sources) + " 2> " + args.destination +  "/" + destination + ".err"

parcreatecmd = "par2 c -n1 -r5 -vv " + args.destination + "/" + destination + ".tar"
parverifycmd = "par2 v -vv " + args.destination + "/" + destination + ".tar"

if (args.tryonly):
    print(bupcmd)
    print(parcreatecmd)
    print(parverifycmd)
else:
    cmd = bupcmd + " && " + parcreatecmd + " && " + parverifycmd
    subprocess.call(cmd, shell = True)



