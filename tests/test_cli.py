import appyqt.cli as cli
import appyqt.asyncTools as asytools
def test_loadingCircle():
    cli.loadingCircle("test")
    cli.stopLoadingCircle()
    cli.loadingCircle("test", True)
    cli.stopLoadingCircle()

def test_menu():
    asytools.runFunctionAsync(cli.menu, "Test", "Test", ["test1", "test2"])