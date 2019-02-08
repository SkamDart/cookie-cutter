from setuptools import (
    find_packages,
    setup
)

AUTHOR = '{AUTHOR}'
VERSION = '{VERSION}'


config = {
    'name': '{project_name}',
    'description': 'project description',
    'version': VERSION,
    'author': AUTHOR,
    'install_requires': [],
    'dependency_links': [],
    'packages': find_packages(exclude=('tests', 'docs')),
    'test_suite': 'tests',
    'scripts': []
}

setup(**config)
