# DICOM-Manager
DICOM Manager is a CLI tool to read and modify DICOM.

```
usage: dicom-manager [-h] [-d DIRECTORY] [-l {DICOMDIR,dcm}] [-r {DICOMDIR,dcm,selection}] [-a] [--createDICOMDIR]

options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Specify the DICOM directroy path.
  -l {DICOMDIR,dcm}, --locate {DICOMDIR,dcm}
                        Locate DICOMDIR or dcm files.
  -r {DICOMDIR,dcm,selection}, --read {DICOMDIR,dcm,selection}
                        Read DICOMDIR, all dcm files or select a file to read.
  -a, --anonymize       Anonymize DICOM files.
  --createDICOMDIR      Creates a DICOMDIR.
```

In order to use `--createDICOMDIR` option and create a DICOMDIR from the dcm files, you must have dcmtk installed on your computer.

## Installation

To install dcmtk, which is required for some feature, see the installation page on [Download of DCMTK Tools](https://dcmtk.org/en/dcmtk/dcmtk-tools/).

For Arch Linux, you will find it in the AUR:

```
paru -S dcmtk-git
```

It is recommended to install DICOM-Manager in a Python virtual environment.

```
python -m venv Dicom-Manager
source Dicom-Manager/bin/activate
pip install git+https://github.com/fantomH/DICOM-Manager.git
```
