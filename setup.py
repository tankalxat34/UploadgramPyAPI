from setuptools import setup, find_packages
from os.path import join, dirname

setup(name='UploadgramPyAPI',
 
      version='1.0',
 
      url='https://github.com/tankalxat34/UploadgramPyAPI',
 
      license='MIT',
 
      author='tankalxat34',
 
      author_email='tankalxat34@gmail.com',
 
      description='This API can be upload, download, remove and rename any files from the service uploadgram.me. Using programming language: Python.',
 
      packages=find_packages(exclude=['tests']),
 
      long_description=open('README.md').read(),
 
      zip_safe=False,
 
      setup_requires=['nose>=1.0'],
 
      test_suite='nose.collector')