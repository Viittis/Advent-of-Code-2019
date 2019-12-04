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
    for wire in data_in:
        cur_wire = []
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

                cur_wire.append((x,y))

        wire_points.append(cur_wire)
    return wire_points


# Return manhattan distance
def manhattan_distance(vectors):
    values = []
    for vector in vectors:
        values.append(abs(vector[0]) + abs(vector[1]))
    values.sort()
    return values[0]


# Return only intersecting values
def intersect_lists(list_in):
    s1 = set(list_in[0])
    s2 = set(list_in[1])
    return (list(s1.intersection(s2)))


# Main
def main():
    start_time = time()

    # Load puzzle input
    wires = load_data("data.txt")

    # Get all wirepoints
    points = map_wire_points(wires)

    # Intersecting values
    duplicates = intersect_lists(points)

    result = manhattan_distance(duplicates)

    print(f"Result = {result}. Calculated in {(time()-start_time)} seconds.")

if __name__ == '__main__':
    main()