class House:  # Builder
    def __init__(self):
        self.walls = None
        self.roof = None
        self.windows = None
        self.doors = None

    def __str__(self):
        return f"House with {self.walls} walls, {self.roof} roof, {self.windows} windows, and {self.doors} doors."

class HouseBuilder:  # Concrete Builder
    def __init__(self):
        self.house = House()

    def build_walls(self, walls):
        self.house.walls = walls
        return self

    def build_roof(self, roof):
        self.house.roof = roof
        return self

    def build_windows(self, windows):
        self.house.windows = windows
        return self

    def build_doors(self, doors):
        self.house.doors = doors
        return self

    def get_house(self):
        return self.house

class Director:  # Director
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_walls("brick").build_roof("shingle").build_windows(4).build_doors(2)
        return self.builder.get_house()

# Usage
builder = HouseBuilder()
director = Director(builder)
house = director.construct()
print(house)


## Output
# House with brick walls, shingle roof, 4 windows, and 2 doors.
