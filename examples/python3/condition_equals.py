
#x description="'==' vs 'is'"

#x pre={
l1 = [1, 2, 3]
l2 = l1
l3 = [1, 2, 3]

print(l1 == l2)
print(l1 == l3)

print(l1 is l2)
print(l1 is l3)
#x }

#x step={
print(l1 == l2) # True
print(l1 == l3) # True

print(l1 is l2) # True
print(l1 is l3) # False
#x }

#x explanation="'==' checks for equality, 'is' checks for identity"

