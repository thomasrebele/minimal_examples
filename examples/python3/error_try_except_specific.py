
#x description="deal with specific exception"
#x pre={
# f = open('/tmp/myfile.txt')
# catch IOError
#x }

#x step={
try:
    f = open('/tmp/myfile.txt')
except IOError as e:
    print("I/O error {}".format(e))
#x }

