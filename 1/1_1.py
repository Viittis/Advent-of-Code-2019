from time import time

# External file for data
data_in = "data.txt"

# Read every line from txt file
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        for line in curfile.readlines():
            data.append(line)
    return data

# Calculate fuel need for module
def calc_mass(module_mass):
    fuel_needed = int(module_mass // 3) - 2
    #print(fuel_needed)
    return fuel_needed

# Main
start_time = time()
fuel_need = 0

#modules = [12, 14, 1969, 100756]
modules = load_data(data_in)

for module in modules:
    fuel_need += calc_mass(int(module))


print(f"Total fuel need = {fuel_need}. Calculated in {(time()-start_time)} seconds.")