#!usr/bin/python
import sys
import os.path
import re
import fileinput


SETTINGS_PATH = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else 'settings.py'

for line in fileinput.input(SETTINGS_PATH, inplace=1):
    line = re.sub(r'#\s.*$', '', line)
    print line,

for line in fileinput.input(SETTINGS_PATH, inplace=1):
    if line.rstrip():
        print line,

pattern1 = re.compile('[A-Z]|\(')
pattern2 = re.compile('\)|\}')
for line in fileinput.input(SETTINGS_PATH, inplace=1):
    if pattern1.match(line):
        print line
    elif pattern2.match(line):
        print "\n", line
    else:
        print line,
