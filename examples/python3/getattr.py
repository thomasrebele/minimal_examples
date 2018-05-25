
#x description="call a method of an instance dynamically"

#x pre={
obj = "abc"
attr = "upper"

# fn = ...
#x }

#x step={
fn = getattr(obj, attr)
#x }

#x post={
upper = fn()
#x }

print(upper)
