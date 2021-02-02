#!/usr/bin/env python

"""The setup script."""

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3.7', ]

setup(
    author="LINHD POSTDATA Project",
    author_email='info@linhd.uned.es',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Utilities',
    ],
    description="Sentiment analysis and hate speech detection library.",
    install_requires=read("requirements.txt").split("\n"),
    license="Apache Software License 2.0",
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges',
                   re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('HISTORY.rst'))
    ),
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='daltons',
    name='daltons',
    packages=find_packages(include=['daltons', 'daltons.*']),
    py_modules=[splitext(basename(path))[0] for path in glob('daltons/*.py')],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/linhd-postdata/daltons',
    version='0.0.1',
    zip_safe=False,
)
