
#x description="walk over two iterators at the same time"


#x pre={
it1 = iter([1,2,3])
it2 = iter(["a", "b", "c"])

#x }


#x step={
it_both = zip(it1, it2)
#x }

#x post={
# iterate over it1, then it2
for i in it_both:
    print(i)

# outputs
# (1, 'a')
# (2, 'b')
# (3, 'c')
#x }


