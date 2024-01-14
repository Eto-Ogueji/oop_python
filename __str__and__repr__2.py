class A:
    def __str__(self):
        return "42"
    
a = A()
print(repr(a)) # <__main__.A object and memory>

print(str(a))