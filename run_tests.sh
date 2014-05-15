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
chmod +x bootstrap.py manage.py

# build it
./bootstrap.py
./manage.py collectstatic --noinput

# run our tests (finally!)
make


