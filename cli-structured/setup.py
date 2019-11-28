from pip._internal.req import parse_requirements
from setuptools import setup, find_packages

raw_requirements = parse_requirements('requirements/dev.txt', session=False)
requirements = [str(ir.req) for ir in raw_requirements]

with open("../README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='foo',
    version='1.0.0',
    scripts=['scripts/build_foo.py'] ,
    author="odelucca",
    author_email="deluccafonseca@gmail.com",
    description="Foo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
