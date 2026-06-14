"""APPYQT's ASync function system, using Threading as a backend. (not asyncio)"""

import threading
import typing
from . import cli

funcDone = threading.Event()


def runFunctionAsync(function: typing.Callable, name: str, *args):
    """Runs a Python function asynchronously, with a loader. (from appyqt.cli) Please don't print anything in the function as it can break the loading circle. Use for I/O stuff like network requests and file operations only. :D"""
    thread = threading.Thread(target=function, daemon=True, args=args)
    thread.start()
    cli.loadingCircle(name)
    while thread.is_alive():
        pass
    cli.stopLoadingCircle()