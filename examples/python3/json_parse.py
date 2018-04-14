
#x description="read content of a file"
#x pre={
fname = "readme.txt"
data = '["foo", {"bar":["baz", null, 1.0, 2]}]'
#x }

#x step={
import json
dictionary = json.loads(data)
#x }

