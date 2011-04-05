#!/usr/bin/env python
import os
import sys
import subprocess
import shutil

pwd = os.path.dirname(__file__)
vedir = os.path.join(pwd,"ve")

if os.path.exists(vedir):
    shutil.rmtree(vedir)

ret = subprocess.call(["python",os.path.join(pwd,"pip.py"),"install",
                       "-E",os.path.join(pwd,"ve"),
                       "--enable-site-packages",
                       "--index-url=''",
                       "--requirement",os.path.join(pwd,"requirements/apps.txt")])
if ret: exit(ret)

ret = subprocess.call([os.path.join(vedir,"bin/easy_install"),
                       '-f',os.path.join(pwd,"requirements/eggs/"),
                       'egenix-mx-base',
                       ])
exit(ret)
