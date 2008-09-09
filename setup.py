from setuptools import setup, find_packages

setup(name='ccnmtldjango',
      version="0.1",
      author="anders pearson",
      description="Django template for CCNMTL",
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      zip_safe=False,
      entry_points="""
      [paste.paster_create_template]
      ccnmtldjango = ccnmtldjango:CcnmtlDjangoTemplate
      """
      )
	
