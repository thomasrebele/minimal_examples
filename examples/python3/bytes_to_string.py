
#x description="bytes to string"
#x pre={
data=b"hello world"
#x }

#x step={
string=data.decode("utf-8")
#x }

print(string)
