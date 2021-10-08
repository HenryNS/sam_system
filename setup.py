from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read
    
setup(
name = "samsystem",
version = "0.0.0",
description ="scanning system for high speed high resolution aquisition",
long_description = long_description,
author = "Henry Cowan",
author_email = "henry.cowan@novosound.net",
url = 'https://github.com/HenryNS/sam_system',
packages=find_packages(include=['pipython', 'libtiepie']),
install_requires = [
    "matplotlib",
    "numpy",
    "serial",
    "pandas",
    "pyserial",
    "scipy",
    ],
scripts = [
    "Scripts/sample.py"
        ]
)
