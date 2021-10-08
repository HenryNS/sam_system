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
install_requires = [
    "matplotlib",
    "numpy",
    "serial",
    "pandas",
    "pyserial",
    "scipy",
    "libtiepie @ git+https://github.com/TiePie/python-libtiepie.git@master",
    ],

scripts = [
    "Scripts/sample.py"
        ]
)
