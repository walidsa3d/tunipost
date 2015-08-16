from setuptools import setup, find_packages

data_files = [
    ('share/doc/tunipost', ['README.md'])
]

setup(
    name='tunipost',
    version='0.9',
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
    data_files=data_files,
    entry_points={"console_scripts": [""]},
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
