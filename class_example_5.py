class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot('" + self.name + "', " + str(self.build_year) + ")"
    
    def __str__(self):
        return "Name: " + self.name + ", Build Year: " + str(self.build_year)
    

if __name__ == "__main__":
    x = Robot("Marvin", 1979)
    x_str = str(x)
    print(x_str)
    print()