from setuptools import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='doggy',
    version='1.0.2',
    homepage="https://github.com/orangeappleak/PYTHON-CLI",
    url="https://github.com/orangeappleak/PYTHON-CLI",
    author="A.Karthik A.K.A REDMANGOAPPLE",
    author_email="redmaniac0510@gmail.com",
    description="A python package that helps you set shortcuts for your project folders or file editors(its still in development)",
    long_description=long_description,
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