
#x description="generator comprehension"
#x pre={
l = [1, 2, 3, 4]

# generator that squares items in l?
#x }

#x step={
g = (x**2 for x in l)
#x }

#x post={
# list(g) == [1, 4, 9, 16]
#x }

print(list(g))


