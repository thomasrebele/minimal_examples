
#x description="recursive generator"

#x pre={
def binaries(n, b = ""):
    if n == 0: yield b
    else:
        # ...
        # ...
#x }
        pass

#x step={
def binaries(n, b = ""):
    if n == 0: yield b
    else:
        yield from binaries(n-1, b + "0")
        yield from binaries(n-1, b + "1")
#x }

#x post={
for c in binaries(3):
    print(c)

# outputs
# 000
# 001
# ...
#x }


