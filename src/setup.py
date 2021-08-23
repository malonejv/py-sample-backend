from setuptools import find_packages, setup

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.9']
 
VERSION = '1.0.0'

setup(name='sample-backend',
    version=VERSION,
    description='Sample backend for todo-list application',
    #long_description=open('README.txt').read() + '\n\n' +
    #open('CHANGELOG.txt').read(),
    url='https://github.com/malonejv/py-sample-backend',  
    author='Javier López Malone',
    author_email='malonejv@gmail.com',
    license='MIT', 
    classifiers=classifiers,
    keywords=['todolist','todo'], 
    packages=find_packages(),
    install_requires=[''])
