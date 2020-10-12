from setuptools import setup

setup(
    name='doggy',
    version='0.2.4',
    py_modules=['doggy'],
    install_requires=[
        'Click',
        'colorama',
        'json'
    ],
    entry_points={
        'console_scripts': [
            'doggy=doggy:main_commands',
        ],
    },
)