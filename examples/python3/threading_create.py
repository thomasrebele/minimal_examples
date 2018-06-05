
#x description="create a thread"

#x pre={
def run():
    print("I'm a new thread")

import threading
#x }

#x step={
thread = threading.Thread(name='example', target=run)
#x }

#x post={
thread.start()
#x }


