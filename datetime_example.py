import datetime
# wrong
# today = datetime.datetime.now()
# str_s = str(today)

# print(eval(str_s))

# the datetime module can only be applied on the strings created by repr
# correct

today = datetime.datetime.now()
repr_s = repr(today)
t = eval(repr_s)
print(type(t))