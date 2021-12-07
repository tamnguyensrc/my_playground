"""Setup file for project"""
from setuptools import setup, find_packages


def readme():
    """Include README.rst content in PyPi build information"""
    with open('README.md') as file:
        return file.read()


setup(
    name='my_playground',
    version='0.0.1',
    author='Infra',
    author_email='tam.nguye@is.com',
    description='Python playground!',
    long_description=readme(),
    long_description_content_type="text/markdown",
    url='https://github.com/tamnguyensrc/my_playground.git',
    packages=find_packages(exclude=["tests*"]),
    entry_points={
        'console_scripts': [
            'greet = src.greet:main'
        ]
    },
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ]
)
