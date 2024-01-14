# use this to print the dictionary key, value pair of the classname.__class__.__dict__ dictionary
class Robot:
    pass

for k, w in Robot.__class__.__dict__.items():
    print("Key: {} has a value of {}".format(k, w))
    print("\n")

# to lazy to research the differences
# for k, w in Robot.__dict__.items():
#     print("Key: {} has a value of {}".format(k, w))
#     print("\n")