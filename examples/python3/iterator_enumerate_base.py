
#x description="iterate over list with 1-based index"
#x pre={
l = ["apple", "banana", "cherry", "date"]

# print items and their index, starting with 1?
#x }

#x step={
for idx, item in enumerate(l, 1):
    print(str(idx) + ": " + item)
#x }

#x post={
# outputs
# 1: apple
# 2: banana
# 3: cherry
# 4: date
#x }



