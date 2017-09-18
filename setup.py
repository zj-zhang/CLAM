#!/usr/bin/env python

from setuptools import setup


def main():
	setup(name='CLAM',
		  version='1.1.0',
		  description='CLIP-seq Analysis of Multi-mapped reads',
		  author='Zijun Zhang',
		  author_email='zj.z@ucla.edu',
		  url='https://github.com/Xinglab/CLAM',
		  packages=['CLAM', 'CLAM.stats'],
		  scripts=['bin/CLAM']
		 )
	return

if __name__ == '__main__':
	main()