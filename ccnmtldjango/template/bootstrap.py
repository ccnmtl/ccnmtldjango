#!/usr/bin/env python
import os
import sys
import subprocess

pwd = os.path.dirname(__file__)
vedir = os.path.join(pwd,"ve")

try:
    os.removedirs(vedir)
except:
    pass

subprocess.call(["python",os.path.join(pwd,"create-ve.py")])
subprocess.call(["python",os.path.join(pwd,"ve-bootstrap.py"),vedir])
