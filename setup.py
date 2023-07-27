#!/usr/bin/env python

from setuptools import setup, find_packages  # type: ignore

with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    author="TheToddLuci0",
    author_email="email@example.com",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],
    description="Request a SSH certificate from a lambda",
    entry_points={
        "console_scripts": [
            "request-ssh-certificate=request_ssh_certificate.cli:main",
        ],
    },
    install_requires=['boto3'],
    license="MIT license",
    long_description=readme,
    long_description_content_type="text/markdown",
    package_data={"request_ssh_certificate": ["py.typed"]},
    include_package_data=True,
    keywords="request_ssh_certificate",
    name="request_ssh_certificate",
    package_dir={"": "src"},
    # packages=find_packages(
    #     include=["src/request_ssh_certificate", "src/request_ssh_certificate.*"]
    # ),
    setup_requires=[],
    url="https://github.com/TheToddLuci0/request_ssh_certificate",
    version="0.1.1",
    zip_safe=False,
)
