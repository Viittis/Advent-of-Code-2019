from time import time


# Read txt file into a list
def load_data(file_in):
    data = []
    with open(file_in) as cur_file:
        for line in cur_file.read().splitlines():
            planet, child = line.split(")")

            planets = [x[0] for x in data]

            if planet in planets:
                i = planets.index(planet)
                data[i][1].append(child)
            else:
                data.append((planet,[child]))
    return data


def find_parent(orbits):

    parents = set([x[0] for x in orbits])
    children = set([y for y in x[1] for x in orbits])

    return list(parents.intersection(children))


# Main
def main():

    # Load puzzle input
    planets = load_data("example.txt")

    print(find_parent(planets))


if __name__ == '__main__':
    main()