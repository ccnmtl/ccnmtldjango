#!/usr/bin/env python
import os
import sys
import subprocess
import shutil

pwd = os.path.dirname(__file__)
vedir = os.path.join(pwd,"ve")

if os.path.exists(vedir):
    shutil.rmtree(vedir)

subprocess.call(["python",os.path.join(pwd,"create-ve.py")])
subprocess.call(["python",os.path.join(pwd,"ve-bootstrap.py"),vedir])
