#!/usr/bin/env python
import os
import sys
import subprocess
import shutil

pwd = os.path.abspath(os.path.dirname(__file__))
vedir = os.path.abspath(os.path.join(pwd,"ve"))

if os.path.exists(vedir):
    shutil.rmtree(vedir)

virtualenv_support_dir = os.path.abspath(os.path.join(pwd, "requirements", "virtualenv_support"))

ret = subprocess.call(["python", "virtualenv.py", 
                       "--extra-search-dir=%s" % virtualenv_support_dir,
                       "--never-download",
                       vedir])
if ret: exit(ret)

ret = subprocess.call([os.path.join(vedir, 'bin', 'pip'), "install",
                       "-E", vedir,
                       "--enable-site-packages",
                       "--index-url=''",
                       "--requirement",os.path.join(pwd,"requirements/apps.txt")])
if ret: exit(ret)

def has_eggs():
    return ".egg" in [os.path.splitext(f)[1] 
                      for f 
                      in os.listdir(os.path.join(pwd,"requirements/eggs/"))]

if has_eggs():
    # only try to easy install eggs if there actually are some
    ret = subprocess.call([os.path.join(vedir,"bin/easy_install"),
                           '-f',os.path.join(pwd,"requirements/eggs/")])
    exit(ret)
