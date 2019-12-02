from time import time

# External file for data
data_in = "data.txt"


# Read txt file into an array
def load_data(file_in):
    data = []

    with open(file_in) as curfile:
        for line in curfile.read().split(','):
            data.append(int(line))

    return do_replacements(data)


# Do specified replacements
def do_replacements(code_in):
    replacements = [(1, 12), (2, 2)]

    for x in replacements:
        code_in[x[0]] = x[1]

    return code_in


# Handle intcode
def handle_intcode(code_in):
    i = 0

    while i < len(code_in):
        if code_in[i] == 1:
            code_in[code_in[i + 3]] = code_in[code_in[i + 1]] + code_in[code_in[i + 2]]
        elif code_in[i] == 2:
            code_in[code_in[i + 3]] = code_in[code_in[i + 1]] * code_in[code_in[i + 2]]
        elif code_in[i] == 99:
            return code_in[0]
        else:
            print(f"Faulty code = {code_in[0]}")
            break
        i += 4


# Main
start_time = time()

int_code = load_data(data_in)

result = handle_intcode(int_code)

print(f"Result = {result}. Calculated in {(time()-start_time)} seconds.")