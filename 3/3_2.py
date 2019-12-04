from time import time

# Read txt file into an array
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        for line in curfile.read().splitlines():
            data.append(line.split(","))
    return data


# Wires to wirepoints
def map_wire_points(data_in):
    wire_points = []
    for index, wire in enumerate(data_in):
        x = 0
        y = 0
        steps = 0
        for wire_point in wire:
            dir = wire_point[0]
            length = int(wire_point[1:])
            for step in range(length):
                if dir == "U":
                    y += 1
                if dir == "D":
                    y -= 1
                if dir == "L":
                    x -= 1
                if dir == "R":
                    x += 1

                steps += 1

                wire_points.append(Wirepoint(index, x, y, steps))

    return wire_points

# Return only intersecting values
def intersect_lists(list_in):

    datalist = []
    datalist.append([(i.x,i.y) for i in list_in if i.wire == 0])
    datalist.append([(i.x,i.y) for i in list_in if i.wire == 1])

    s1 = set(datalist[0])
    s2 = set(datalist[1])
    return (list(s1.intersection(s2)))

# Class for wirepoints
class Wirepoint():
    def __init__(self, wire, x, y, steps):
        self.wire = wire
        self.x = x
        self.y = y
        self.steps = steps


# Main
def main():
    start_time = time()

    # Load puzzle input
    wires = load_data("data.txt")

    # Get all wirepoints
    points = map_wire_points(wires)

    # Intersecting values
    shared_wirepoints = intersect_lists(points)

    totals = []

    for wp in shared_wirepoints:
        matching_points = filter(lambda x: x.x == wp[0] and x.y == wp[1], points)
        steps = 0
        for item in matching_points:
            steps += item.steps
        totals.append(steps)

    result = (min(totals))

    print(f"Result = {result}. Calculated in {(time()-start_time)} seconds.")


if __name__ == '__main__':
    main()