
#x description="comprehension with condition"
#x pre={
l = [1, 2, 3, 4]

# list of squares of even numbers in l?
#x }

#x step={
s = [x**2 for x in l if x % 2 == 0]
#x }

#x post={
# s == [4, 16]
#x }

print(s)


