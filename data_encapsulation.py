class Robot:
    def __init__(self, name=None, build_year=None):
        self.name = name
        self.build_year = build_year

    def say_hi(self):
        if self.name:
            print("Hi, I am " + self.name)

        else:
            print("Hi, I am a robot without a name")

        if self.build_year:
            print("I was built in " + str(self.build_year))
        else:
            print("It's not known, when I was created")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_build_year(self, build_year):
        self.build_year = build_year

    def get_build_year(self):
        return self.build_year


x = Robot("ETG-V1", 2025)
y = Robot()
z = Robot()


y.set_name("ETG-V2")

z.set_name(y.get_name())
z.set_build_year(x.get_build_year())

x.say_hi()
y.say_hi()
print(z.get_build_year())

