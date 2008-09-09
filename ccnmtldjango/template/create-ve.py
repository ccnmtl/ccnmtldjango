import virtualenv, textwrap
output = virtualenv.create_bootstrap_script(textwrap.dedent("""
import os, subprocess, glob
import os.path

def after_install(options,home_dir):
    print "eggsdir: " + os.path.join(os.path.dirname(__file__),'eggs')
    eggs = glob.glob(os.path.join(os.path.dirname(__file__),'eggs','*.egg'))
    subprocess.call([join(home_dir, 'bin', 'easy_install')] + ['-H','None','-f',os.path.join(os.path.dirname(__file__),'eggs')] + eggs)

"""))
f = open('ve-bootstrap.py','w').write(output)
