from time import time
from operator import add, mul


# External file for data
data_in = "data.txt"


# Read txt file into an array
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        for line in curfile.read().split(','):
            data.append(int(line))
    return data


# Parse instructions
def parse_instructions(instructions_in):

    instructions_out = []

    opcode = instructions_in % 100
    param1 = instructions_in // 100 % 10
    param2 = instructions_in // 1000 % 10
    param3 = instructions_in // 10000 % 10

    return [opcode, param1, param2, param3]


# Calculate
def do_calc(value1, opcode, value2):
    operators = {1: add, 2: mul}
    op = operators[opcode]
    return op(value1, value2)


# Parse intcode
def parse_intcode(intcode_in, comp_input):
    i = 0

    while True:
        # returns a list in format [opcode, param1, param2, param3]
        params = parse_instructions(intcode_in[i])
        opcode = params[0]

        if opcode == 99:
            return dg_code

        # Assign values
        noun = i + 1 if params[1] else intcode_in[i + 1]
        verb = i + 2 if params[2] else intcode_in[i + 2]
        write_to = i + 3 if params[3]  else intcode_in[i + 3]

        if opcode == 1 or opcode == 2:
            intcode_in[write_to] = do_calc(intcode_in[noun], opcode, intcode_in[verb])
            i += 4
        elif opcode == 3:
            intcode_in[noun] = comp_input
            i += 2
        elif opcode == 4:
            dg_code = intcode_in[noun]
            i += 2
        elif opcode == 5: # jump if true
            if intcode_in[noun]:
                i = intcode_in[verb]
            else:
                i += 3
        elif opcode == 6: # jump if false
            if intcode_in[noun] == 0:
                i = intcode_in[verb]
            else:
                i += 3
        elif opcode == 7: # less than
            if intcode_in[noun] < intcode_in[verb]:
                intcode_in[write_to] = 1
            else:
                intcode_in[write_to] = 0
            i += 4
        elif opcode == 8: # equals
            if intcode_in[noun] == intcode_in[verb]:
                intcode_in[write_to] = 1
            else:
                intcode_in[write_to] = 0
            i += 4
        else:
            print("ERROR:", opcode)
            break

# Main
def main():
    start_time = time()

    # Puzzle input/data
    int_code = load_data(data_in)
    computer_input = 5

    result = parse_intcode(int_code, computer_input)

    print(f"Diagnostic code = {result}. Calculated in {(time() - start_time)} seconds.")


if __name__ == '__main__':
    main()