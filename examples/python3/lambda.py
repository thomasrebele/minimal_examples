
#x description="lambda function"

#x pre={
def square(n):
    return n**2

# write as square = ...
#x }

#x step={
square = lambda n: n**2
#x }

print(square(2))
