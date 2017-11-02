#!/usr/bin/env python3
locations = [r'C:\Program Files (x86)\SmartSynchronize\bin\smartsynchronizec.exe']

import hashlib
import sys
import subprocess
import os
import shutil

def hashFile(filename):
  m = hashlib.md5()
  with open(filename, 'rb') as f:
    m.update(f.read() + str(os.path.getmtime(filename)).encode('utf8'))
  return m.digest()

local = sys.argv[1]
base = sys.argv[2]
other = sys.argv[3]

validLocations = list(filter(os.path.exists, locations))
if len(validLocations) == 0:
  print("SmartSynchronize not found.")
  sys.exit(1)
smartsync = validLocations[0]

oldhash = hashFile(base)
# Works on Windows according to (IRC nick) Zephtar (orignial author)
#cmd = '"%s" "%s" "%s" "%s"' % (smartsync, local, base, other)
# Works on OS X and Correct according to doc:
# http://docs.python.org/library/subprocess.html#subprocess.Popen
cmd = (smartsync, local, other, base)
p = subprocess.Popen(cmd)
p.wait()
newhash = hashFile(base)

if oldhash == newhash:
  sys.exit(1)
else:
  shutil.copyfile(base, local)
  sys.exit(0)
