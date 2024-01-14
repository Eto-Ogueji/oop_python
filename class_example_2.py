class Robot:
    pass

x = Robot()
y = Robot()

x.name = "ETG-V1"
x.build_year = "2025"

y.name = "ETG-V2"
y.build_year = "2025"


# print(x.name)
# print(y.build_year)

# for k, w in Robot.__dict__.items():
#     print("Key: {} has a value of {}".format(k, w))
#     print("\n")

for k, w in Robot.__class__.__dict__.items():
    print("Key: {} has a value of {}".format(k, w))
    print("\n")