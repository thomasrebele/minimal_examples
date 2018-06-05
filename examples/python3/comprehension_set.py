
#x description="set comprehension"
#x pre={
l = [1, 2, 3, 4]

# set of squares of l?
#x }

#x step={
s = {x**2 for x in l}
#x }

#x post={
# s == set([1, 4, 9, 16])
#x }

print(s)


