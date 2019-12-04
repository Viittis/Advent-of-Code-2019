from time import time

# External file for data
data_in = "data.txt"

# Read txt file into an array
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        for line in curfile.read().splitlines():
            data.append(line.split(","))
    return data

# Wirepoints to numeric values
def map_wire_points(data_in):
    wire_points = []
    for wire in data_in:
        x = 0
        y = 0
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
                wire_points.append((x,y))

    return wire_points

def manhattan_distance(vectors):
    values = []
    for vector in vectors:
        values.append(abs(vector[0]) + abs(vector[1]))
    values.sort()
    return values[0]

def remove_duplicates(data_in):
    uniques = set(data_in[0])
    uniques.update(data_in[1])

    duplicates = []

    for list in data_in:
        for coords in list:
            if coords not in uniques:
                duplicates.append(coords)

    return duplicates

# Main
def main():
    start_time = time()

    #wires = load_data(data_in)

    wires = []
    wires.append(["R98", "U47", "R26", "D63", "R33", "U87", "L62", "D20", "R33", "U53", "R51"])
    wires.append(["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"])

    #wires.append(["R8","U5","L5","D3"])
    #wires.append(["U7","R6","D4","L4"])

    points = map_wire_points(wires)
    print("Removing duplicates....")

    #duplicates = [x for x in points[0] if x in points[1]]
    duplicates = remove_duplicates(points)
    print("ok")

    result = manhattan_distance(duplicates)

    print(f"Result = {result}. Calculated in {(time()-start_time)} seconds.")

if __name__ == '__main__':
    main()