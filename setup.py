# Automatically created by: shub deploy

from setuptools import setup, find_packages

setup(
    name         = 'virgin_mobile_gear_stores',
    version      = '1.1',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = virgin_mobile_gear_stores.settings']},
    package_data = {
        'package' : '*csv',
    },
    include_package_data=True,
)
