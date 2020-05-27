import re
import argparse
from datetime import datetime

"""
Author: Zack Knight
    Program to clean the process hacker output. 
    Only accepts one command line argument, which is the input file.
    Not stress tested. Literally written in 5 minutes.
    Not robust at all.

    You need to delete the top lines of the process hacker output yourself.

    This part:
    Process Hacker 2.39.124
    Windows NT 6.1 Service Pack 1 (64-bit)
    5/15/2020 2:52:48 PM
"""

parser = argparse.ArgumentParser()
parser.add_argument('in_file',help='Input file')

args = parser.parse_args()
print(args)
inFile = args.in_file

with open(inFile,'r') as fp:
    lines = fp.readlines()

for x in range(len(lines)):
    lines[x] = lines[x].strip()

pattern = re.compile(r'^0x.*\ \([0-9]*\): ')

subbedLines = []

for line in lines:
    subbedLines.append(re.sub(pattern,"",line))

date = datetime.now().strftime("%Y%m%d-%H%M")
out = f"Outfile({date}).txt"

with open(out,'w') as fp:
    for x in subbedLines:
        fp.write(x+"\n")

print(f"Done. Written to {out}")