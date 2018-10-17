#!/usr/bin/env python3

from setuptools import setup, find_packages


setup(
    name='stackby',
    version='0.3',
    description='Instant coding answers via the command line',
    long_description='python command line appliation to stack and cleanup files into different directories based on type, extension and created date',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",   
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3.6",
        "Topic :: System :: Filesystems",
        "License :: OSI Approved :: MIT License"
    ],
    keywords='stack files directories cleanup',
    author='Musthaq Ahamad',
    author_email='musthu.gm@gmail.com',
    maintainer='Musthaq Ahamad',
    maintainer_email='musthu.gm@gmail.com',
    url='https://github.com/haxzie/stackby',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'stackby = stackby.stackby:main',
        ]
    },
    install_requires=[
        'fire','python-magic','libmagic'
    ]
)
