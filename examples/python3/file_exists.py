
#x description="check whether a file exists"
#x pre={
fname="readme.txt"
#x }

#x step={
import os.path
exists = os.path.isfile(fname)
#x }

