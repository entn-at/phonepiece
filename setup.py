from setuptools import setup,find_packages

requirements=[r.strip() for r in open("requirements.txt").readlines()]

setup(
   name='phonepiece',
   version='1.0.9',
   description='a multilingual phone tokenizer',
   author='Xinjian Li',
   author_email='xinjianl@cs.cmu.edu',
   url="https://github.com/xinjli/phonepiece",
   packages=find_packages(),
   install_requires=requirements,
   package_data={'': ['*.csv', '*.tsv', 'tree.txt']},
   include_package_data=True,
)
