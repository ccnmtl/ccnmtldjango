from setuptools import setup, find_packages

setup(name='ccnmtldjango',
      version="2.0.0",
      author="Anders Pearson",
      author_email='ctl-dev@columbia.edu',
      description='Paste template for Django development at CCNMTL',
      long_description=open('README.md').read(),
      url='https://github.com/ccnmtl/ccnmtldjango/',
      packages=find_packages(),
      install_requires = ["PasteScript"],
      zip_safe=False,
      package_data = {'' : ['*.*']},
      include_package_data=True,
      entry_points="""
      [paste.paster_create_template]
      ccnmtldjango = ccnmtldjango:CcnmtlDjangoTemplate
      """
      )
