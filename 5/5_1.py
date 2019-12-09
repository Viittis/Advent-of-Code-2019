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


# Parse opcode
def parse_opcode(opcode_in):
    data_out = []

    # Opcode
    str_opcode = str(opcode_in)
    opcode = str_opcode[-2:] if str_opcode[-2:] else None

    # Params
    i = 0
    params = str_opcode[-(len(opcode)+1)::-1]
    while i < len(params):
        if i == (len(params)-2):
            if params[i+1] == '-':
                value = params[i+1] + params[i]
                i += 1
            else:
                value = params[i]
        else:
            value = params[i]
        i += 1
        data_out.append(int(value))

    # If there's less than 3 params, add zeroes to reach len=3
    while len(data_out) < 3:
        data_out.append(0)

    return int(opcode), data_out


# Calculate
def do_calc(value1, opcode, value2):
    operators = {1: add, 2: mul}
    op = operators[opcode]
    return op(value1, value2)


# Parse intcode
def parse_intcode(intcode_in, comp_input):
    i = 0
    while i < len(intcode_in):
        # returns a list in format [opcode, [3 params] *default param 0]
        opcode, parameters = parse_opcode(intcode_in[i])

        if opcode == 1 or opcode == 2:
            dataset_size = 4
            write_to = intcode_in[i+3] # if parameters[2] == 0 else intcode_in[i+3]
            value2 = intcode_in[intcode_in[i+2]] if parameters[1] == 0 else intcode_in[i+2]
            value1 = intcode_in[intcode_in[i+1]] if parameters[0] == 0 else intcode_in[i+1]
            intcode_in[write_to] = do_calc(value1, opcode, value2)
        elif opcode == 3:
            dataset_size = 2
            intcode_in[intcode_in[i + 1]] = comp_input
        elif opcode == 4:
            dataset_size = 2
            print(intcode_in[intcode_in[i + 1]])
        elif opcode == 99:
            return True
        else:
            dataset_size = 1
            print("ERROR")
            break

        i += dataset_size


# Main
def main():
    start_time = time()

    # Puzzle input/data
    int_code = load_data(data_in)
    computer_input = 1

    complete = parse_intcode(int_code, computer_input)

    print(f"Ready. Calculated in {(time() - start_time)} seconds.")


if __name__ == '__main__':
    main()