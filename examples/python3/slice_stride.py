
#x description="list stride"
#x pre={
l = ["a", "b", "c", "d", "e", "f"]

# get every other element, i.e., ["a", "c", "e"]
#x }

#x step={
r = l[::2]
#x }

print(r)

#x explanation="[start:end:stride]"
