
#x description="check whether a collection is empty"

#x pre={
s = set()
l = []

# s empty? l empty?
#x }

#x step={
if not s:
    print("s is empty")

if not l:
    print("l is empty")
#x }


