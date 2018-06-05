
#x description="iterate over list with index"
#x pre={
l = ["apple", "banana", "cherry", "date"]

# print items and their index?
#x }

#x step={
for idx, item in enumerate(l):
    print(str(idx) + ": " + item)
#x }

#x post={
# outputs
# 0: apple
# 1: banana
# 2: cherry
# 3: date
#x }



