
#x description="let thread run"

#x pre={
def run():
    print("I'm a new thread")

import threading
thread = threading.Thread(name='example', target=run)
#x }

#x step={
thread.start()
#x }

