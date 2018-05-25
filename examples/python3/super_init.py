
#x description="call init of base class"

#x pre={
class Base:
    def __init__(self, msg):
        print("hello "  + str(msg))

class Child(Base):
    def __init__(self, msg):
        # call base init
#x }

#x step={
        super().__init__(msg)
#x }

#x post={
Child("world!")
#x }

