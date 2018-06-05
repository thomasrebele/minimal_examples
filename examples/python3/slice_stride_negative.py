
#x description="negative list stride"
#x pre={
l = ["a", "b", "c", "d", "e", "f"]
r = l[::-2]

# r?
#x }

#x step={
# ['f', 'd', 'b']
#x }

print(r)

#x explanation="negative stride starts at end"

