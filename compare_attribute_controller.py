import ast
import attribute_controller as ac
import os
import sys
sys.path.append(os.getenv('PACKAGE_PATH'))
sys.path.append(os.getenv('WORKING_DIR'))

import stub_laod

if __name__ == '__main__':

    module = stub_laod.load_module('\\attribute_controller\\__init__.pyi')

    cwapi3d_package = [(node.name, ast.unparse(node.args))
                       for node in module.body if isinstance(node, ast.FunctionDef)]

    cwapi3d_built_in = dir(ac)

    cwapi3d_package_dict = dict(cwapi3d_package)
    cwapi3d_built_in_set = set(cwapi3d_built_in)

    difference = cwapi3d_built_in_set - set(cwapi3d_package_dict.keys())

    for function_name in difference:
        print(f"Missing function name: {function_name}")
