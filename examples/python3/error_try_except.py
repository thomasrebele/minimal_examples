
#x description="deal with exception"
#x pre={
#x }

#x step={
try:
    f = open('/tmp/myfile.txt')
except IOError as e:
    print("I/O error ({0}): {1}".format(e.errno, e.strerror))
#x }

