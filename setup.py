#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('requirements/prod.txt') as prod_requirements_file:
    prod_requirements = prod_requirements_file.read().splitlines()
    if prod_requirements and prod_requirements[0].startswith('-r'):
        prod_requirements = prod_requirements[1:]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Antoine HAMON",
    author_email='antoine.hamon@protonmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3.8',
    ],
    description="Classification d'offres d'emploi.",
    install_requires=prod_requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='offerclassif',
    name='offerclassif',
    packages=find_packages(include=['offerclassif', 'offerclassif.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ZwAnto/offer-classif',
    version='0.1.0',
    zip_safe=False,
)
