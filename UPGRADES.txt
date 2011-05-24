Here's how to upgrade a project built from ccnmtldjango.  Make sure
you run these upgrades one at a time, starting from the earliest
upgrade that your project needs to run.

0.12 -> 0.13
============

How to upgrade a project to the mxDateTime-free psycopg2 egg and conditional easy_install process:

 cd /tmp
 wget --no-check-certificate https://github.com/ccnmtl/ccnmtldjango/tarball/0.13.1
 tar -xzf 0.13.1
 cd ccnmtl-ccnmtldjango-b787e14/ccnmtldjango/template
 cp bootstrap.py /path/to/my/project
 cp requirements/src/psycopg2-2.4-no-mx.tar.gz /path/to/my/project
 ## replace line requirements/src/psycopg2-2.2.1.tar.gz with requirements/src/psycopg2-2.4-no-mx.tar.gz
 vi /path/to/my/project/requirements/libs.txt 
 # make sure it works
 ./bootstrap.py
 git add bootstrap.py requirements/libs.txt requirements/src/psycopg2-2.4-no-mx.tar.gz
 git rm requirements/src/psycopg2-2.2.1.tar.gz requirements/eggs/egenix_mx_base-3.1.3-py2.6-linux-x86_64.egg
 git commit -m "upgrade psycopg2; remove mx dependency; only easy_install eggs if any are present"
 git push

0.11 -> 0.12
============

How to upgrade a project to the fully pinned bootstrapping process:

 cd /tmp
 wget --no-check-certificate https://github.com/ccnmtl/ccnmtldjango/tarball/0.12.0
 tar -xzf 0.12.0
 cd ccnmtl-ccnmtldjango-14bbc77/ccnmtldjango/template
 cp bootstrap.py virtualenv.py /path/to/my/project/
 cp -r requirements/virtualenv_support /path/to/my/project/requirements/
 cd /path/to/my/project/
 # make sure it works; you may need to add more pinned dependency sdists since it's
 # stricter now -- so run bootstrap.py and find/add sdists until it builds successfully
 ./bootstrap.py
 git add bootstrap.py virtualenv.py requirements/virtualenv_support
 git rm pip.py
 git commit -m "update to fully-pinned bootstrap process"
 git push
