from time import time

# External file for data
data_in = "data.txt"

# Read every line from txt file into an array
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        for line in curfile.readlines():
            data.append(line)
    return data

# Calculate the fuel need for a single module
def calc_fuel(module_mass):
    fuel_needed = int(module_mass // 3) - 2
    return fuel_needed

# Main
start_time = time()
total_fuel = 0

modules = load_data(data_in)

for module in modules:
    fuel_need = calc_fuel(int(module))

    while fuel_need > 0:
        total_fuel += fuel_need
        fuel_need = calc_fuel(fuel_need)

print(f"Total fuel need = {total_fuel}. Calculated in {(time()-start_time)} seconds.")