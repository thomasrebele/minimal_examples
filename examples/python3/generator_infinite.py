# https://stackoverflow.com/a/5739258/1562506


#x description="infinite 0 generator"

#x step={
g = iter(int, 1)
#x }

import itertools

#x post={
for i in itertools.islice(g, 0, 4):
    print(i)

# outputs
# 0
# 0
# 0
# 0
#x }

#x explanation="iter calls function until it returns the second argument (sentinel)"

