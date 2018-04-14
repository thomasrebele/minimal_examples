
#x description="split a string on whitespace characters"
#x pre={
data="some spaces  and tabs  end"
#x }

#x step={
import re
regex = re.compile("\\s+")
lst = regex.split(data)
#x }

print(lst)

