import ast
import os
import sys

sys.path.append(os.getenv('PACKAGE_PATH'))

from dotenv import load_dotenv


def load_module(path_to_pyi: str) -> ast.Module:
    load_dotenv('D:\\Python\\cwapi3d_compare\\.env')
    path = os.getenv('PACKAGE_PATH')
    path += path_to_pyi
    with open(path) as f:
        module = ast.parse(f.read())
    return module
