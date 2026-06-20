# APPYQT CLI

## Loading Circle

The loading circle shows a CLI loading circle that's asyncrounous.

### Start loading circle

```python
import appyqt.cli as cli

cli.loadingCircle("Doing something...") # Start loading circle, you can add True as second arg to make the circle a small variant

# do I/O

# stop loading circle

```

**== OR ==**

```python
import appyqt.cli as cli

cli.loadingCircle("Doing something...", True) # Start small loading circle

# do I/O

# stop loading circle

```

This function (`appyqt.cli.loadingCircle`) shows a loading circle. IMPORTANT: DO NOT PRINT ANYTHING DURING THE LOADING CIRCLE

### Stop running loading circle

```python
import appyqt.cli as cli

cli.loadingCircle("Doing something...") # Start loading circle, you can add True as second arg to make the circle a small variant

# do I/O

cli.stopLoadingCircle() # gives ===Info=== Completed task "Doing something..." in x seconds ===

```

This function (`cli.stopLoadingCircle()`) stops a loading circle.