# cwapi3d_compare Project

This project is used to compare the functions in the built-in `cwapi3d` module with the functions defined in a .pyi stub file. 
It prints the names of the functions that are in the attribute_controller module but not in the stub file.  

stub_load.py: This file contains a function load_module() that loads a .pyi stub file and 
parses it into an Abstract Syntax Tree (AST) using the ast module in Python.  

## Usage
Set the PACKAGE_PATH and WORKING_DIR environment variables in your .env file. 
PACKAGE_PATH should be the path to your Python site-packages directory, 
and WORKING_DIR should be the path to the directory where your project is located.  

## Requirements
To install the requirements from a requirements.txt file, you can use the following command in your terminal:
``` pip install -r requirements.txt ```