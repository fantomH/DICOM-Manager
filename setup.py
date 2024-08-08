# :----------------------------------------------------------------------- INFO
# :[dicom_manager/setup.py]
# :author        : Pascal Malouin
# :created       : 2023-05-26 16:36:50 UTC
# :updated       : 2024-08-08 19:12:12 UTC
# :description   : Setup script for dicom_manager

from setuptools import (
    setup,
    find_packages
)

setup(
    name='DICOM-Manager',
    version='1.0.1',
    packages=find_packages(),
    author="Pascal Malouin",
    author_email="pascal.malouin@gmail.com",
    description="DICOM Manager is a CLI tool to read and modify DICOM.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/fantomH/DICOM-Manager/",
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pydicom',
        'python-magic',
    ],
    entry_points={
        'console_scripts': [
            'dicom-manager=dicom_manager:main',
        ]
    }
)
