from setuptools import setup
import setuptools

setup(
    name='doggy',
    version='0.3.3',
    py_modules=['doggy'],
    packages=setuptools.find_packages(include=["commands"]),
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