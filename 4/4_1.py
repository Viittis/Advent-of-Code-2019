from time import time

# Validate pw against given rules
def validate_pw(pw_in):
    list = [x for x in str(pw_in)]
    for i in range(1, len(list)):
        if int(list[i]) < int(list[i - 1]):
            return False
    return True

# Main
def main():
    start_time = time()
    pw_start = 147981
    pw_end = 691423
    matches = 0

    for pw in range(pw_start,pw_end+1):
        if(validate_pw(pw)):
            matches += 1

    print(matches)

if __name__ == '__main__':
    main()