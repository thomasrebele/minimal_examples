
#x description="walk over two iterators at the same time exhaustively"


#x pre={
it1 = iter([1, 2, 3, 4])
it2 = iter(["a", "b", "c"])

#x }


#x step={
from itertools import zip_longest
it_both = zip_longest(it1, it2)
#x }

#x post={
# iterate over it1, then it2
for i in it_both:
    print(i)

# outputs
# (1, 'a')
# (2, 'b')
# (3, 'c')
# (4, None)
#x }


