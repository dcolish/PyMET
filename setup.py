"""
PyMET
------
A python library for talking to the `trimet api`_

.. _`trimet api`: http://developer.trimet.org/

Links
`````

* `development version
  <http://github.com/dcolish/pymet/zipball/master#egg=PyMet-dev>`_
"""

from setuptools import setup, find_packages

setup(
    name="pymet",
    version="dev",
    packages=find_packages(),
    namespace_packages=['pymet'],
    include_package_data=True,
    author="Dan Colish",
    author_email="dcolish@gmail.com",
    description="API wrapper for PyMET data",
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    license='BSD',
    url='http://www.github.com/dcolish/pymet',

    classifiers=[
        'Development Status :: 4 - Beta ',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        ],

    entry_points={
        'console_scripts': [
            'pymet=pymet.pymet:main',
            ],
        },

    install_requires=[
        'beautifulsoup',
        'inflect',
        ],
    )
