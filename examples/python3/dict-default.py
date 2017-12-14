
#x description="default value for dict"

#x pre={
d = {"a": 1, "b": 2}

# get value of "c", or 0 if not in dictionary
# c = d ...
#x }

#x step={
c = d.get("c", 0)
#x }


