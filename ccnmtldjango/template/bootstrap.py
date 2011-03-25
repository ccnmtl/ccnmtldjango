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

import virtualenv, textwrap
output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess, glob
import os.path

def after_install(options,home_dir):
    ret = subprocess.call([os.path.join(home_dir, 'bin', 'pip'), "install",
                          "-E", home_dir,
                          "--enable-site-packages",
                          "--index-url=''",
                          "-r", os.path.join("%(pwd)s", "requirements/apps.txt")])
    if ret: exit(ret)
    ret = subprocess.call([os.path.join(home_dir, 'bin', 'easy_install'),
                           os.path.join("%(pwd)s", "requirements/eggs/egenix_mx_base-3.1.3-py2.6-linux-x86_64.egg")])
    exit(ret)
""" % locals()))

fd, bootscript = tempfile.mkstemp(".py")
os.write(fd, output)
os.close(fd)

subprocess.call(["python2.6", bootscript, "-vvv", "--setuptools-egg-path", os.path.join(pwd, "setuptools-0.6c11-py2.6.egg"), vedir])

