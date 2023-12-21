import ast
import os

import attribute_controller as ac

import sys
sys.path.append('D:\\Python\\PycharmProjects\\cwapi3d_compare\\Lib\\site-packages')

from dotenv import load_dotenv

if __name__ == '__main__':

    load_dotenv('D:\\Python\\cwapi3d_compare\\.env')

    path = os.getenv('PACKAGE_PATH')
    path += '\\attribute_controller\\__init__.pyi'
    with open(path) as f:
        module = ast.parse(f.read())

    cwapi3d_package = [(node.name, ast.unparse(node.args))
                       for node in module.body if isinstance(node, ast.FunctionDef)]

    cwapi3d_built_in = dir(ac)

    cwapi3d_package_dict = dict(cwapi3d_package)
    cwapi3d_built_in_set = set(cwapi3d_built_in)

    difference = cwapi3d_built_in_set - set(cwapi3d_package_dict.keys())

    for function_name in difference:
        print(f"Missing function name: {function_name}")
