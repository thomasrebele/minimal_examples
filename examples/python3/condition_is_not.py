
#x description="'not' and 'is'"

#x pre={
l1 = [1, 2, 3]
l2 = [1, 2, 3]

print(not l1 is l2)
# pythonic way?
#x }

#x step={
print(l1 is not l2)
#x }

#x post={
# outputs True
#x }

