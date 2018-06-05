
#x description="semantics of try (2)"

#x pre={
try:
    raise Exception()
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
# B
# D
#x }


