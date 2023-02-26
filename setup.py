from setuptools import setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name='pfile',
    version='0.1.0',    
    description='A File reading Python package',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/shuds13/pyexample',
    author='Vidya Sagar',
    author_email='shudson@anl.gov',
    license='Komhar',
    packages=['pfile'],
    
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Komhar',  
        'Operating System :: OS Independent',        
        'Programming Language :: Python :: 3.10',
        
    ],
)