
#x description="parse a date"
#x pre={
d = '2005-06-01 15:33'
#x }

#x step={
from datetime import datetime
date_and_time = datetime.strptime(d, '%Y-%m-%d  %H:%M')
#x }

print(date_and_time)

