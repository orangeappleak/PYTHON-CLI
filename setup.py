from setuptools import setup

setup(
    name='doggy',
    version='0.2.3',
    py_modules=['doggy'],
    install_requires=[
        'Click',
        'colorama'
    ],
    entry_points='''
        [console_scripts]
        doggy=doggy:cli
    ''',
)