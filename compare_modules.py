import ast
import attribute_controller as ac
import cadwork
import element_controller as ec
import os
import sys

# set path to package
sys.path.append('D:\\Python\\PycharmProjects\\cwapi3d_compare\\Lib\\site-packages')

from dotenv import load_dotenv

load_dotenv('D:\\Python\\cwapi3d_compare\\.env')

sys.path.append(os.getenv('WORKING_DIR'))

import stub_laod

if __name__ == '__main__':

    module_cadwork = stub_laod.load_module('\\cadwork\\__init__.pyi')

    difference_cadwork = stub_laod.get_function_difference(module_cadwork, cadwork)
    for function_name in difference_cadwork:
        print(f"Missing function name: {function_name}")

    print()

    module_element = stub_laod.load_module('\\element_controller\\__init__.pyi')

    difference_element = stub_laod.get_function_difference(module_element, ec)
    for function_name in difference_element:
        print(f"Missing function name: {function_name}")




