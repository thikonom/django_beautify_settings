#!usr/bin/env python

import sys
import os.path
import re
import fileinput

if len(sys.argv) > 1:
    SETTINGS_PATH = os.path.abspath(sys.argv[1])
else:
    SETTINGS_PATH = 'settings.py'

for line in fileinput.input(SETTINGS_PATH, inplace=1):
    line = re.sub(r'#\s.*$', '', line)
    print line,

for line in fileinput.input(SETTINGS_PATH, inplace=1):
    if line.rstrip():
        print line,

pattern1 = re.compile(r'[A-Z]|\(')
pattern2 = re.compile(r'\)|\}')
for line in fileinput.input(SETTINGS_PATH, inplace=1):
    if pattern1.match(line):
        print line
    elif pattern2.match(line):
        print "\n", line
    else:
        print line,
