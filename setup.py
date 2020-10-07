from setuptools import setup

setup(
    name='init',
    version='0.1',
    py_modules=['init'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        init=init:hello
    ''',
)