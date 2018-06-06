
#x description="deal with exception"

#x pre={
# f = open('/tmp/myfile.txt')
#x }

#x step={
try:
    f = open('/tmp/myfile.txt')
except:
    print("error opening file")
#x }

#x explanation="better: except certain error types, e.g., IOError"

