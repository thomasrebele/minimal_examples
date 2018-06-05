
#x description="search for a pattern in a string"
#x pre={
data=" he was the governor from 2004 to 2010, and  ..."

import re
regex = re.compile("from ([0-9]+) to ([0-9]+), ")
# task: extract 2004 and 2010
#x }

#x step={
m = regex.search(data)
first  = m.group(1)
second = m.group(2)
#x }

print(first)
print(second)

