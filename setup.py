# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def readme_to_md(file='README.md'):
    read_md = None

    try:
        from pydoc import convert
        read_md = convert(file, 'rst', 'md')

    except ImportError:
        print("warning: pypandoc module not found, could not convert Markdown to RST")
        read_md = open(file, 'r').read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sample',
    version='0.0.4',
    description='Random work',
    long_description=readme_to_md('README.md'),
    author='tkolleh',
    author_email='tinatuh@gmail.com',
    url='https://github.com/tkolleh/FunWithEuler',
    license=license
)
