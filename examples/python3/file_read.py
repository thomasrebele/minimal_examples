
#x description="read content of a file"
#x pre={
fname="readme.txt"
#x }

#x step={
with open(fname, 'r') as myfile:
    content = myfile.read()
#x }

