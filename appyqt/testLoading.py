import cli
import time

cli.loadingCircle("Doing")
time.sleep(2)
#cli.stopAllLoadingCircles()

cli.loadingCircle("Doing some more.")
time.sleep(5)
cli.stopLoadingCircle()