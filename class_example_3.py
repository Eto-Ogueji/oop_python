class Robot:
    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)
        else:
            print("Hi, I am a robot without name")

x = Robot()
x.say_hi()

y = Robot("ETG")
y.say_hi()