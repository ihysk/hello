from setuptools import setup


setup(
    name='hello',
    version='0.0.1',
    packages='',
    entry_points={
        'console_scripts': [
            'hello=hello.hello:hello',
        ],
    },
)
