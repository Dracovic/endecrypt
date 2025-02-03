from setuptools import setup, find_packages

setup(
    name="endecrypt",
    version="0.1",
    packages=find_packages(where="my_cryptography/py"),
    package_dir={"": "my_cryptography/py"},
)