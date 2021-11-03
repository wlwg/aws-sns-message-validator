from datetime import datetime
from setuptools import setup, find_packages

DEPENDENCIES = [
    'requests>=2.24.0',
    'cryptography>=3.3.2',
]

EXCLUDED_PACKAGES = [
    'flask_example.py',
]

setup(
    name='aws-sns-message-validator',
    version='0.0.3',
    description='Validator for SNS messages.',
    author='https://github.com/wlwg',
    url='https://github.com/wlwg/sns-message-validator',
    python_requires='>=3.6',
    install_requires=DEPENDENCIES,
    packages=find_packages(exclude=EXCLUDED_PACKAGES),
)
