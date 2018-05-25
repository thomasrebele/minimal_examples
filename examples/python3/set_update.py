
#x description="add elements to set"

#x pre={
s = set([1,2,3])
l = [4,5,6]

# add l to s
#x }

#x step={
s.update(l)
#x }

print(s)

