
#x description="lambda function with capture"

#x pre={
add = {}
for i in [1,2]:
    # return a function f(n) that calculates i+n
#x }

#x step={
    add[i] = lambda n, i=i: i+n
#x }


print(add[1](9))
print(add[2](8))

#x explanation="i=i is necessary, otherwise both lambdas use i=2"

