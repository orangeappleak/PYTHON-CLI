from setuptools import setup
import setuptools

setup(
    name='doggy',
    version='0.3.9',
    py_modules=['doggy'],
    packages=setuptools.find_packages(),
    install_requires=[
        'Click',
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'doggy=doggy:main_commands',
        ],
    },
)