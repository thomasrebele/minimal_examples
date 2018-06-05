
#x description="semantics of try (1)"

#x pre={
try:
    print("A")
except:
    print("B")
else:
    print("C")
finally:
    print("D")

# output?
#x }

#x step={
# A
# C
# D
#x }


