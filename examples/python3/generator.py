
#x description="simple generator"

#x step={
def cube(n):
    for i in range(n):
        yield i**3
#x }

#x post={
for c in cube(5):
    print(c)
#x }
