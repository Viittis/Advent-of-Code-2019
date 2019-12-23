
def test1():
    tlist = []
    tlist.append(["1","1","2","1","2","0"])
    tlist.append(["1","2","3","4","5","0"])

    for item in tlist:
        print(any([item[i],item[i]] == item[i:i+2] for i in range(len(item) - 1)))

def test2():
    tlist = 12687651123113132341142
    str_tlist = [x for x in str(tlist)]

    # Iteroidaan kirjain kerrallaan
    for i in range(len(str_tlist) - 1):
        # Tehdään kunnes breakataan
        while True:
            if str_tlist[i] == str_tlist[i+1]:
                i += 1
            else:
                break

# Read txt file into a list
def load_data(file_in):
    planets = []
    with open(file_in) as curfile:
        for line in curfile.read().splitlines():
            data = line.split(")")
            planet = Planet(data[0])
            planet.add_child(data[1])

            planet_names = [x.name for x in planets]

            if planet.name not in planet_names:
                planets.append(planet)
            else:
                i = planet_names.index(planet.name)
                planets[i].add_child(data[1])

    return planets

# Class for planets
class Planet:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, new_child):
        self.children.append(new_child)

test2()