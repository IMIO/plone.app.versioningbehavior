# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os


version = '1.4.1.dev0'

tests_require = [
    'plone.app.testing',
    'Products.CMFDiffTool',
    'Products.CMFEditions [test]',
    'Products.CMFPlone',
    'plone.app.dexterity',
    'plone.app.testing',
    'plone.namedfile[blobs]',
]

setup(
    name='plone.app.versioningbehavior',
    version=version,
    description=('Provides a behavior for using CMFEditions with '
                 'dexterity content types'),
    long_description=(open('README.rst').read() + '\n' +
                      open(os.path.join('CHANGES.rst')).read()),
    # Get more strings from
    # https://pypi.org/classifiers/
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Plone',
        'Framework :: Plone :: 5.0',
        'Framework :: Plone :: 5.1',
        'Framework :: Plone :: 5.2',
        'Framework :: Plone :: Core',
        'Framework :: Zope2',
        'Framework :: Zope :: 4',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone dexterity behavior versioning CMFEditions',
    author='Jonas Baumann, 4teamwork GmbH',
    author_email='mailto:dexterity-development@googlegroups.com',
    url='http://plone.org/products/dexterity',
    license='GPL version 2',
    packages=find_packages(),
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.app.dexterity[relations]',
        'plone.autoform',
        'plone.behavior>=1.1',
        'plone.dexterity',
        'plone.namedfile[blobs]',
        'plone.rfc822',
        'Products.CMFEditions>2.2.9',
        'setuptools',
        'zope.container',
    ],
    tests_require=tests_require,
    extras_require=dict(tests=tests_require),
    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
