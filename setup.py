from setuptools import setup

version = '0.1'

setup(
    name='Flask-Compass',
    version=version,
    url='https://github.com/zerok/flask-compass',
    license='BSD',
    author='Horst Gutmann',
    author_email='zerok@zerokspot.com',
    description='Adds automatic Compass compilation to Flask',
    long_description=__doc__,
    packages=['flaskext'],
    namespace_packages=['flaskext'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)