from setuptools import setup, find_packages

setup(
    name="django_loaddata_stdin",
    version="0.0.1",
    description="Django module to load data from stdin",
    url='https://github.com/squareweave/django-loaddata-stdin',
    author='Squareweave',
    author_email='team@squareweave.com.au',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages('django_loaddata_stdin'),
    install_requires=['django >= 1.8'],
)
