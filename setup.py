from setuptools import setup, find_packages

setup(name='ccnmtldjango',
      version="1.0.4",
      author="Anders Pearson",
      description='Paste template for Django development at CCNMTL',
      long_description=open('README.md').read(),
      url='http://github.com/ccnmtl/ccnmtldjango/',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      install_requires = ["PasteScript"],
      zip_safe=False,
      package_data = {'' : ['*.*']},
      include_package_data=True,
      entry_points="""
      [paste.paster_create_template]
      ccnmtldjango = ccnmtldjango:CcnmtlDjangoTemplate
      """
      )
