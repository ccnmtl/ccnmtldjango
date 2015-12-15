#!/bin/bash

# install ccnmtldjango into an outer virtualenv
rm -rf temp/
mkdir temp
virtualenv temp/outer-ve
./temp/outer-ve/bin/python setup.py develop

# then use that to make a test application
cd temp
./outer-ve/bin/paster create --template=ccnmtldjango testproject
cd testproject
make init

# run our tests (finally!)
make


