
#x description="create a thread"

#x pre={
def todo():
    print("I'm a new thread")

import threading
#x }

#x step={
thread = threading.Thread(name='example', target=todo)
#x }

#x post={
thread.start()
#x }


