import importlib
import sys

print("Welcome to APPYQQT! GitHub: https://github.com/ApplePair111/appyqt")

# sys.modules.pop(__name__)  # remove from cache, forces re-run next import

def addTool(path: str):
    # "functions.math.equations" -> from mylib.functions.math.equations import *
    module = importlib.import_module(f"mylib.{path}")
    current = sys.modules[__name__]
    
    for attr in dir(module):
        if not attr.startswith("_"):
            setattr(current, attr, getattr(module, attr))
