import ast
import os
import sys

sys.path.append(os.getenv('PACKAGE_PATH'))

from dotenv import load_dotenv


def load_module(path_to_pyi: str) -> ast.Module:
    path = os.getenv('PACKAGE_PATH')
    path += path_to_pyi
    with open(path) as f:
        module = ast.parse(f.read())
    return module


def get_function_difference(module: ast.Module, controller) -> set[str]:
    cwapi3d_package = [(node.name, ast.unparse(node.args))
                       for node in module.body if isinstance(node, ast.FunctionDef)]

    cwapi3d_built_in = dir(controller)

    cwapi3d_package_dict = dict(cwapi3d_package)
    cwapi3d_built_in_set = set(cwapi3d_built_in)

    return cwapi3d_built_in_set - set(cwapi3d_package_dict.keys())
