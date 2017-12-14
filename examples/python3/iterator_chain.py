
#x description="concatenate iterators"


#x pre={
it1 = iter([1,2,3])
it2 = iter([4,5,6])

# import ...
# it_both = ...
#x }


#x step={
import itertools

it_both = itertools.chain(it1, it2)
#x }

#x post={
# iterate over it1, then it2
for i in it_both:
    print(i)
#
