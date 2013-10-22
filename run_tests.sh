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
chmod +x bootstrap.py manage.py build_lettuce_db.sh

# build it
./bootstrap.py

# run our tests (finally!)
./manage.py test
./manage.py jenkins
./manage.py collectstatic --no-input
./build_lettuce_db.sh
LETTUCE_SKIP_SELENIUM=1 ./manage.py harvest --settings=testproject.settings_lettuce --verbosity=3; rm -f /tmp/lettuce-django.pid
./ve/bin/flake8 testproject
