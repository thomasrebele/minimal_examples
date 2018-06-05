
#x description="dict comprehension"
#x pre={
l = [1, 2, 3, 4]

# dictionary of items in l to their square?
#x }

#x step={
d = {x:x**2 for x in l}
#x }

#x post={
# d == {1:1, 2:4, 3:9, 4:16}
#x }

print(d)


