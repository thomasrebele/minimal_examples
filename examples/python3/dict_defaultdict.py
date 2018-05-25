#x description="dict with default value"

#x pre={
# from collections import ...
#x }

#x step={
from collections import defaultdict

d = defaultdict(lambda: 0)
#x }

