from setuptools import setup, find_packages


setup(
    name='hello',

    version='0.0.1',

    description='Hello!',
    long_description='Just say Hello',

    url='https://github.com/sirouma/hello',

    author='siro_uma',
    author_email='siro_uma@example.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Training',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    keywords='hello',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'hello=hello.hello:hello',
        ],
    },
)
