from setuptools import setup, find_packages

with open('README.md') as readme, \
     open('requirements.txt') as requirements:
    setup(
        name="django_loaddata_stdin",
        version="0.0.4",
        description="Django module to load data from stdin",
        long_description=readme.read(),
        url='https://github.com/squareweave/django-loaddata-stdin',
        author='Squareweave',
        author_email='team@squareweave.com.au',
        license='BSD',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ],
        packages=find_packages(),
        install_requires=requirements.readlines(),
    )
