
#x description="lambda function with capture"

#x pre={
add = {}
for i in [0,1,2]:
    # return a function f(n) that calculates i+n
#x }

#x step={
    add[i] = lambda n, i=i: i+n
#x }

#x post={
print(add[2](7))

# outputs 10
#x }

#x explanation="i=i is necessary, otherwise the lambdas use i=2"

