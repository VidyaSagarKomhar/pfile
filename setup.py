from setuptools import setup

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name='pfile',
    version='0.1.0',    
    description='A File reading Python package',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url='https://github.com/VidyaSagarKomhar/pfile.git@v0.1.0-beta',
    author='VidyaSagarKomhar',
    author_email='vidya.sagar@komhar.com',
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
