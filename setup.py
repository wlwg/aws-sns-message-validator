from datetime import datetime
from setuptools import setup, find_packages

DEPENDENCIES = [
    'requests==2.21.0',
    'cryptography==2.6.1',
]

EXCLUDED_PACKAGES = [
    'flask_example.py',
]

setup(
    name='sns-message-verification',
    version='0.0.1',
    description='Verification for SNS messages.',
    author='https://github.com/wlwg',
    url='https://github.com/wlwg/sns-message-verification',
    python_requires='>=3.7',
    install_requires=DEPENDENCIES,
    packages=find_packages(exclude=EXCLUDED_PACKAGES),
)
