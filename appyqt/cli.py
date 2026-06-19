"""
APPYQT's CLI app tools!
"""

from blessed import Terminal
import threading as thr
import sys
import time

term = Terminal()

def menu(title: str, items: list):
    """
    Show an interactive menu with options. If choice exists, returns choice index from list in args. For example, menu("Example", ["choice 1", "choice 2"]) returns 0 if choice 1, returns 1 if choice 2. Returns None if escaped or interrupted.
    """
    sel = 0
    with term.fullscreen(), term.cbreak(), term.hidden_cursor():
        while True:
            print(term.home + term.clear)
            print(term.bold_yellow(title) + '\n')
            for i, item in enumerate(items):
                if i == sel:
                    print(term.bold_blue(f'❯ {item}'))
                else:
                    print(f'  {item}')
            print(f'\n{term.dim("Enter to confirm · Esc to cancel")}')

            key = term.inkey()
            if key.code == term.KEY_UP:   sel = max(0, sel - 1)
            if key.code == term.KEY_DOWN: sel = min(len(items)-1, sel+1)
            if key == '\n' or key.code == term.KEY_ENTER: return sel
            if key.code == term.KEY_ESCAPE: return None

stopLoading = thr.Event()
doneLoading = thr.Event()

patternLarge = ('⡿','⣟','⣯','⣷','⣾','⣽','⣻','⢿')
patternSmall =  ('⠟','⠯','⠷','⠾','⠽','⠻')


def LoadingCircleBackend(text, useSmall):
    start = time.time()
    while not stopLoading.is_set():
        pattern = patternLarge
        if useSmall:
            pattern = patternSmall
        for char in pattern:
            if stopLoading.is_set():
                break
            sys.stdout.write(f"\r\n\n{char}   {text}\n\n")
            sys.stdout.flush()
            time.sleep(0.08)
    sys.stdout.write("\r" + " " * (len(text) + 6) + "\r")
    sys.stdout.flush()
    stopLoading.clear()
    elapsed = time.time() - start
    mins = int(elapsed // 60)
    secs = round(elapsed % 60, 2)

    if mins > 0:
        print(f'===Info=== Completed task "{text}" in {mins} minutes and {secs} seconds ===')
    else:
        print(f'===Info=== Completed task "{text}" in {secs} seconds ===')
    doneLoading.set()
    return


def loadingCircle(text: str, useSmall: bool = False):
    """Makes a loading circle like in npm. Arg 1 is for any text. Also, you can put True as useSmall arg to make pattern mini. Thanks to 6 on GitHub for making braille-pattern-cli-loading-indicator. Text from https://github.com/6/braille-pattern-cli-loading-indicator/blob/master/index.js :D"""
    loader = thr.Thread(target=LoadingCircleBackend, daemon=True, args=(text, useSmall))
    loader.start()

def stopLoadingCircle():
    """Stop running loadingCircle()"""
    stopLoading.set()
    doneLoading.wait()
    doneLoading.clear()


def prompt(prompt: str, placeholder: str = ""):
    """
    Prompt for a message from user like input() but look nicer and support placeholders. Placeholder is optional!!
    """

    input(f"❯ {prompt} ❯ {term.dim(placeholder)}❯ ")
    print(f'\n{term.dim("Enter to confirm · Esc to cancel")}')

    key = term.inkey()
    if key.code == term.KEY_ESCAPE: return None