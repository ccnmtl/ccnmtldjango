ccnmtldjango is a Paste Template that we use to replace
the standard `django-admin.py startproject` command. 

It does the same basic task of setting up a directory 
structure for a django app, but it has been extended to
implement a lot of CCNMTL specific functionality 
and configuration. 

What it provides for us that startproject doesn't:

* Django Wind (a Django bridge to Columbia's central auth service - 
  http://www.jasig.org/cas/deployments/columbia-university)
  is included and configured by default so our apps can use WIND
  for auth automatically. Ie, anyone with a Columbia UNI by
  default will have an account. The CCNMTL developer UNIs are
  automatically set up as superusers, and the group affil that
  CCNMTL staff all have gets automatically mapped to staff. These
  are generally useful defaults for us. 
* virtualenv and pip setup with source tarballs bundled and
  bootstrappable, `manage.py`'s shebang set to use it. This
  basically fits it into our one-step automated deployment and
  containment approach.  
* sorl.thumbnail (a handy dandy image thumbnailing library) is included by default
* flatpages enabled
* settings split for dev/prod
* apache/django.wsgi configured
* sample apache config for mod_wsgi setup using Virtual
  Environments (everything is streamlined so that we can just
  symlink the generated apache config file into our production
  server's `/etc/apache/sites-enabled/` directory and it's good to go)
* media dirs for dev and prod configured
* smartif included (https://github.com/thraxil/django-smartif/tree/master)
* template_utils included
  (http://code.google.com/p/django-template-utils/) as well as
  feedparser, which it depends on for feed stuff
* django-typogrify included (http://code.google.com/p/typogrify/)
  along with smartypants.py (which it uses)
* django-sentry included
  (https://github.com/dcramer/django-sentry) and configured for our setup
* django-munin included (https://github.com/ccnmtl/django-munin)
* South is included for database migrations
* uuid.py
* jquery (1.4.2, minified) included
* hs.js
* tabber.js
* widget.js
* tablesort.js	
* required CSS for the above js libraries is included in the
  site.css by default
* base templates included
* django admin enabled (and authenticated with WIND for tlc)
* restclient
* httplib2
* imageuploader
* markdown is included and enabled
* database defaulted to postgresql (cause MySQL is teh suck)
* transaction middleware enabled by default (cause data corruption is teh suck)
* timezone set
* I18n turned off (we are unfortunately monolingual. no sense in denying it)
* PIL
* psycopg2 (stripped of its mx.DateTime dependency)
* a nice default template design with alternate base templates for multi-column layout.

To use ccnmtldjango, you need python 2.6+, virtualenv, pip, and a recent 
setuptools installed on your machine. 

First, if you don't already have ccnmtldjango installed, do

    $ easy_install ccnmtldjango

It should automatically pull in the needed dependencies (just 
PasteScript, actually).

Running

    $ paster create --list-templates

should include ccnmtldjango

Now, to quickstart a django project, do

    $ paster create --template=ccnmtldjango myprojectname

`myprojectname` should be a python module name (ie, lowercase, 
no punctuation, etc). It will create a directory called 
`myprojectname` that has a django project in it.

paster still doesn't do anything with file permissions, so we still 
need to manually set a couple:

    $ cd myprojectname
    $ chmod 755 manage.py bootstrap.py

I couldn't figure out a way to insert random strings into the code via
Paste Template, so one thing that ccnmtldjango is missing compared to
a regular django startproject is that the SECRET_KEY variable in
settings_shared.py is always the same default. That's clearly not a
good idea, so make sure you change that to some other random string
that will be unique to your project. 

This is probably a good point to check the project into version control.

We use containment for django too, with virtualenv:

    $ ./bootstrap.py

That will create a `ve` directory which contains a virtualenv and has
had all the libraries in the `requirements/src` directory installed
into it (this includes django itself). The `ve` directory should never
be checked into svn since it's generated. If you need other libraries
for your application, bundle them up as tarballs and drop them in the
`requirements/src/` directory, add them to `requirements/libs.txt` or
`requirements/apps.txt` (depending on whether they are regular python
libraries or django apps) then re-run `./bootstrap.py`.

Keep in mind that with virtualenv, there's no need to `activate` an
environment. Instead, a ve has a `bin` directory which contains a
python executable. If you use that instead of the system python
executable, it uses the libraries in that virtualenv. 

ccnmtldjango assumes that your project will use a postgresql database
with the same name as your project. So, for our example, you would
then do:

    $ createdb myprojectname

and it is all set to use it:

    $ ./manage.py syncdb

will install the tables that django needs for it's common apps (sites,
sessions, admin, flatpages, etc) and have you create an admin user.

The `./manage.py syncdb` automagically sets up an "example.com"
site. This should be changed to your site domain (e.g. `localhost:8000`)
via the admin console. `http://localhost:8000/admin/sites/site/`. (if it
matters for your application)

Your application is ready to run now:

    $ ./manage.py runserver

will start a server on `http://localhost:8000/`. Going there will give
you a 404 since there's nothing in the application yet, but the admin
app should be accessible (via the user account you created during
syncdb, or via WIND to tlc users (or ones specified in the
`WIND_SUPERUSER_MAPPER_GROUPS` list in `settings_shared.py`). So go ahead
and login to `http://localhost:8000/admin/`

Even without any application specific code, flatpages is included so
you can put content on the web right away.

From this point out, it's basic django development. You'll probably
want to do a `./manage.py startapp` to create your own application
within the project and so on.

--------------------------
Setting up a fresh checkout

The first time you check out an existing ccnmtl-template project from
svn/git:

     $ ./bootstrap.py
     $ ./manage.py runserver <IP Address>:<PORT> 


------------------------------------------
Differences from a standard Django install

Obviously, a bunch of libraries and such have been added and there's
the whole virtualenv thing. There are also some differences from a
standard django project (ie, the result of `django-admin.py startproject`) that you should be awayre of.

First, the settings have been split up to make dev and prod
deployments easier to configure. A regular django install will have
one `settings.py` file that contains all the settings. Django
developers will usually copy that settings file and make changes when
deploying to production. ccnmtldjango takes advantage of the fact that
settings are just python code and can be imported and overridden. So
we have a `settings_shared.py` which contains most of the
settings. `settings.py` (which should be used for development) and
`settings_production.py` then import everything from from
`settings_shared.py`. `settings_production.py` then also overrides any
settings that should be different in the production deployment
(usually paths to templates and media files).

`TransactionMiddleware` is enabled by default. This means that each HTTP
request gets a transaction that commits or rolls back at the end of
the request. The default django setup for some reason does things
"autocommit" style where each database operation runs in its own
transaction, independent of the HTTP request.

The other big difference to be aware of is the top-level `templates`
directory. Standard django procedure is to have a templates directory
in each application in your project that contains the templates for
that application. ccnmtldjango has the top-level templates directory
for a couple reasons. First, since paster only creates the project
level directory and not the application directories, it was the only
way to have it include a default `base.html`, `admin/login.html`,
`registration/login.html` and so on. I also just like the approach of
having a project-level templates directory, especially for the
`base.html` template. Django allows multiple template directories and
searches through them in a predictable order, so you can (and probably
should) still create application level template directories, list them
in `TEMPLATE_DIRS` ahead of the project level one, and override whatever
templates you want in those.

I18N is turned off since it's fairly rare that we do multi-lingual
stuff and it's a performance hit to have it enabled if it's not being
used. If you need to do a multi-lingual django site, just re-enable it
and get to work.


