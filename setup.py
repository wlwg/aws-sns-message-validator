from setuptools import setup, find_packages
from pathlib import Path


LONG_DESCRIPTION = (Path(__file__).parent/'README.md').read_text()

DEPENDENCIES = [
    'requests>=2.24.0',
    'requests-cache>=0.8.0',
    'cryptography>=3.3.2',
]

EXCLUDED_PACKAGES = [
    'flask_example.py',
]

setup(
    name='aws-sns-message-validator',
    version='0.0.5',
    description='Validator for AWS SNS messages.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='https://github.com/wlwg',
    url='https://github.com/wlwg/aws-sns-message-validator',
    python_requires='>=3.6',
    install_requires=DEPENDENCIES,
    packages=find_packages(exclude=EXCLUDED_PACKAGES),
)
