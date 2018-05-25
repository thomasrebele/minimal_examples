
#x description="get the current date"
#x pre={
# from ... import ...
#x }

#x step={
from datetime import datetime
now = datetime.now()
#x }

#x post={
# outputs a time and date like 2018-05-25 11:27:07.265155
#x }

print(now)

