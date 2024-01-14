def f(x):
    f.counter = getattr(f, "counter", 0) + 1

for i in range(10):
    f(i)
print(f.counter)