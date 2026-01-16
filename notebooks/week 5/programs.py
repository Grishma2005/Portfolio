import sys
import os
import shutil
import urllib.request
import urllib.error
from pathlib import Path


sys.argv = ["program.py", "hello", "world"]

import sys
print("Platform:", sys.platform)

import sys

sys.argv = ["program.py", "hello", "world"] # pretend these are your arguments
sys.argv = ["program.py"]
print("Number of arguments:", len(sys.argv) - 1)

import sys

args = sys.argv[1:]
if not args:
    print("Error: no arguments given.")
else:
    shortest = sorted(args, key=len)[0]
    print("Shortest argument:", shortest)

sys.argv = ["program.py", "https://www.youtube.com"]

import sys
import urllib.request
import urllib.error

args = sys.argv[1:]
if not args:
    print("Error: no URL provided.")
else:
    url = args[0]
    try:
        req = urllib.request.Request(url, method="HEAD")
        with urllib.request.urlopen(req, timeout=10) as r:
            code = r.status

        if 200 <= code < 400:
            print("Working website ", code)
        else:
            print("Not working ", code)

    except urllib.error.HTTPError as e:
        print("Website error ", e.code)
    except urllib.error.URLError as e:
        print("Could not reach ", e.reason)

sys.argv = ["program.py", "12", "15.5", "-1", "20"]
import sys

args = sys.argv[1:]
if not args:
    print("Error: no temperatures provided.")
else:
    try:
        temps = [float(x) for x in args]
        print("Min:", min(temps))
        print("Max:", max(temps))
        print("Mean:", sum(temps) / len(temps))
    except ValueError:
        print("Error: all temperatures must be numbers.")