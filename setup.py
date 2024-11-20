from setuptools import setup, find_packages

setup(
    name='astro_constants',
    version='1.0.0',
    description='A Python library for common astronomical and physical constants',
    author='Joe Stem',
    author_email='JoeStem25@gmail.com',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
