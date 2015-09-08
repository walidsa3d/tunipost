from setuptools import setup, find_packages
from tunipost import __version__

setup(
    name='tunipost',
    version=__version__,
    description="Find Tunisian Postal Codes",
    long_description=open('README.md').read(),
    author='Walid Saad',
    author_email='walid.sa3d@gmail.com',
    url='https://github.com/walidsa3d/tunipost',
    # download_url='',
    license="GPL",
    keywords="tunis tunisia postal code",
    packages=find_packages(),
    include_package_data=True,
    entry_points={"console_scripts": ["tunipost=tunipost.cli:main"]},
    classifiers=[
        'Development Status :: 4  - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Utilities'
    ]
)
