
#x description="replace whitespace characters by underscores"
#x pre={
data="some spaces  and tabs  end"
#x }

#x step={
import re
regex = re.compile("\\s+")
new_data = regex.sub("_", data)
#x }

print(new_data)

