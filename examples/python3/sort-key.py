

#x description="sort on second component"

#x pre={
l = [(1,4), (2,5), (3,2)]
#x }

#x step={
s = sorted(l, key=lambda t: t[1])
#x }

print(s)
