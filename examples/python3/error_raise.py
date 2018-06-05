
#x description="throw an exception"

#x pre={
e = RuntimeError("I'm an exception")
#x }

#x step={
raise e
#x }


