#!/usr/bin/env python
import os
import sys
import subprocess
import shutil
import tempfile

pwd = os.path.abspath(os.path.dirname(__file__))
vedir = os.path.abspath(os.path.join(pwd,"ve"))

if os.path.exists(vedir):
    shutil.rmtree(vedir)

ret = subprocess.call(["python", "virtualenv.py", vedir])
if ret: exit(ret)

ret = subprocess.call([os.path.join(vedir, 'bin', 'pip'), "install",
                       "-E", vedir,
                       "--enable-site-packages",
                       "--index-url=''",
                       "-r", os.path.join(pwd, "requirements/apps.txt")])
if ret: exit(ret)

ret = subprocess.call([os.path.join(vedir,"bin/easy_install"),
                       '-f',os.path.join(pwd,"requirements/eggs/"),
                       'egenix-mx-base',
                       ])
exit(ret)
