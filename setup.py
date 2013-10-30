from setuptools import setup, find_packages

setup(name='ccnmtldjango',
      version="1.4.2",
      author="Anders Pearson",
      author_email='anders@columbia.edu',
      description='Paste template for Django development at CCNMTL',
      long_description=open('README.md').read(),
      url='http://github.com/ccnmtl/ccnmtldjango/',
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
