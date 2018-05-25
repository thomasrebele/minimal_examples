
#x description="let thread run"

#x pre={
def todo():
    print("I'm a new thread")

import threading
thread = threading.Thread(name='example', target=todo)
#x }

#x step={
thread.start()
#x }

