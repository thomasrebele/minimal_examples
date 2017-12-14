
#x description="customize with statement"


#x pre={
# import ...

# ...
def prefix_print(prefix):
    def pp(text):
        print(prefix + text)
    print("begin")
# ...
    print("end")
#x }


#x step={
import contextlib

@contextlib.contextmanager
def prefix_print(prefix):
    def pp(text):
        print(prefix + text)
    print("begin")
    yield pp
    print("end")
#x }

#x post={
with prefix_print("hello ") as pprint:
    pprint("world")
#x }
