
#x description="list comprehension with nested loops"
#x pre={
l = [[1, 2], [3, 4]]

# list of squares of all numbers in l?
# s = [x**2 ...]
#x }

#x step={
s = [x**2 for t in l for x in t]
#x }

#x post={
# s == [1, 4, 9, 16]
#x }

print(s)

