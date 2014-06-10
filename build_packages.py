#!/usr/bin/env python
import os
import os.path
import subprocess
import shutil
import sys

pwd = os.path.abspath(os.path.dirname(__file__))
vedir = os.path.abspath(os.path.join(pwd, "ve"))


def clear_dist_and_build():
    if os.path.exists("dist"):
        shutil.rmtree("dist")
    if os.path.exists("build"):
        shutil.rmtree("build")


def setup_ve():
    """ make a ve with the freshest versions possible of pip/setuptools/virtualenv/wheel"""
    if os.path.exists(vedir):
        shutil.rmtree(vedir)
    subprocess.call(["virtualenv", vedir])
    subprocess.call([os.path.join(vedir, "bin", "pip"), "install", "setuptools", "--upgrade"])
    subprocess.call([os.path.join(vedir, "bin", "pip"), "install", "pip", "--upgrade"])
    subprocess.call([os.path.join(vedir, "bin", "pip"), "install", "virtualenv", "--upgrade"])
    subprocess.call([os.path.join(vedir, "bin", "pip"), "install", "wheel", "--upgrade"])


if __name__ == "__main__":
    setup_ve()
    if len(sys.argv) > 1:
        # upload packages
        subprocess.call([os.path.join(vedir, "bin", "python"), "setup.py", "sdist", "upload"])
        subprocess.call([os.path.join(vedir, "bin", "python"), "setup.py", "bdist_egg", "upload"])
        subprocess.call([os.path.join(vedir, "bin", "python"), "setup.py", "bdist_wheel", "upload"])
    else:
        # just build them
        subprocess.call([os.path.join(vedir, "bin", "python"), "setup.py", "sdist"])
        subprocess.call([os.path.join(vedir, "bin", "python"), "setup.py", "bdist_egg"])
        subprocess.call([os.path.join(vedir, "bin", "python"), "setup.py", "bdist_wheel"])
