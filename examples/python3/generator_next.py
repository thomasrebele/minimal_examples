
#x description="element of generator"

#x pre={
# generates 0 infinitely
g = iter(int, 1)

# get an element of g
#x }

#x step={
n = next(g)
#x }

#x post={
print(n)

# outputs 0
#x }

