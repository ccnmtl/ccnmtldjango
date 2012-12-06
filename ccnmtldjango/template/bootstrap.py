#!/usr/bin/env python
import glob
import os
import subprocess
import shutil

pwd = os.path.abspath(os.path.dirname(__file__))
vedir = os.path.abspath(os.path.join(pwd, "ve"))

if os.path.exists(vedir):
    shutil.rmtree(vedir)

virtualenv_support_dir = os.path.abspath(
    os.path.join(pwd, "requirements", "virtualenv_support"))

ret = subprocess.call(["python", "virtualenv.py",
                       "--extra-search-dir=%s" % virtualenv_support_dir,
                       "--never-download",
                       vedir])
if ret:
    exit(ret)

ret = subprocess.call([os.path.join(vedir, 'bin', 'pip'), "install",
                       "-E", vedir,
                       "--index-url=''",
                       "--requirement",
                       os.path.join(pwd, "requirements/apps.txt")])
if ret:
    exit(ret)


def has_eggs():
    return [os.path.basename(path) for path in
            glob.glob(os.path.join(pwd, "requirements", "eggs", "*.egg"))]

if has_eggs():
    # only try to easy install eggs if there actually are some
    cmd = ([os.path.join(vedir, "bin/easy_install"),
            '-f', os.path.join(pwd, "requirements/eggs/")] +
           has_eggs())
    ret = subprocess.call(cmd)
    exit(ret)

ret = subprocess.call(["python", "virtualenv.py", "--relocatable", vedir])
# --relocatable always complains about activate.csh, which we don't really
# care about. but it means we need to ignore its error messages
