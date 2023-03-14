from importlib.metadata import entry_points
from setuptools import setup, find_packages
import codecs
import os
VERSION = '0.0.1'
DESCRIPTION = 'A basic hello package'
# Setting up
setup(
    name="gub",
    version=VERSION,
    author="Sharukh Rahman",
    author_email="hello.dev.sr@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=['selenium', 'rich', 'click'],
    keywords=['python'],
    entry_points={
        'console_scripts': 'gub=run:App'
    },

    classifiers=[
        "Development Status ::1-Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Macos :: MacoS X",
        "Operating System :: Microsoft :: Windows",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)
