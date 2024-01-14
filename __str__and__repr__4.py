l = [3, 8,  9]

s = repr(l) #'[3, 8, 9]'l

l # [3, 8, 9]
l == eval(s) # True
l == eval(str(l)) # True
