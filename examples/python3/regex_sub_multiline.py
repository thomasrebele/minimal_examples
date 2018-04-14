
#x description="replace x\ny by _"
#x pre={
data="a x\ny b"
#x }

#x step={
import re
regex = re.compile("x\ny")
new_data = regex.sub("_", data)
#x }

print(new_data)

