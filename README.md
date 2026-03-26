# prism
Welcome to the SABL (Sequence Assessment for Barcoded Libraries) package, offered by the Knight Lab at UNC Chapel Hill! This script was developed by Kevin Coghlan (kevinjcoghlan@gmail.com) and is compiled as a Python package.

## Table of Contents
- [Installation](#installation)
- [Documentation](#documentation)
- [Usage](#usage)

## Installation Instructions
A version of Python >= 3.10 is required to use this package. We recommend using [Anaconda](https://www.anaconda.com) to install Python for those new to Python.
1. Open the terminal (MacOS) or Command Prompt (Windows).
2. Create a virtual directory by running `conda create --name myenv` and replacing `myenv` with the name of your desired environment. Then activate the environment using `conda activate myenv`.
2. Download the package by either:
    1. Direct download.
        1. Download the zip from GitHub (Code -> Download ZIP). Unzip the package somewhere (note the extraction path). The extracted package can be deleted after installation. Navigate to this directory.
        2. Install the package using pip. This command will install this package and required dependencies to your Python environment.
            The package path should be the current working directory `.` if cloned using git. Otherwise, replace it with the path to the `sabl` folder.
            
        `pip install .`
        or `pip install /path/to/package/sabl`

   2. Clone this repository (requires git to be installed) with:
      
   `git clone https://github.com/UNC-Knight-Lab/sabl.git`

That's it!

## Usage

### Sample codes and data
Examples for the main module in this package are included in as Jupyer notebooks and Python scripts in the `examples` folder. Sample input data and output analyses are included in the `sample data` folder. 

### Publication and data archive
For more information, we point you to our publication: XYZ. All raw data in our paper is deposited in the following repository: XYZ