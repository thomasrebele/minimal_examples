
#x description="list comprehension"
#x pre={
l = [1, 2, 3, 4]

# list of squares of l?
#x }

#x step={
s = [x**2 for x in l]
#x }

#x post={
# s == [1, 4, 9, 16]
#x }

print(s)

#x explanation="this initializes the whole list; use generator comprehension (...) for lazy evaluation"

