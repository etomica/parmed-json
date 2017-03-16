from setuptools import setup

setup(
    name='parmed_json',
    packages=['parmed_json'],
    install_requires=[
        'numpy',
        'ParmEd'
    ],

    entry_points={
        'console_scripts': [
            'parmed_json=parmed_json:main'
        ]
    }
)