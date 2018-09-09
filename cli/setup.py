from setuptools import setup

setup(
    name='Markdone cli',
    version='0.1',
    py_modules=['markdone'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        markdone=markdone:cli
    ''',
)