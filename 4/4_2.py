from time import time

# Validate pw against given rules
def validate_pw(pw_in):
    pw_list = [x for x in str(pw_in)]

    # Digits increase to the right
    for i in range(1, len(pw_list)):
        if int(pw_list[i]) < int(pw_list[i - 1]):
            return False

    # Password contains at least one pair of digits
    counts = {x: pw_list.count(x) for x in pw_list}

    if 2 in counts.values():
        return True
    else:
        return False

# Main
def main():
    start_time = time()
    pw_start = 147981
    pw_end = 691423
    result = 0

    for pw in range(pw_start,pw_end+1):
        if(validate_pw(pw)):
            result += 1

    print(f"Result = {result}. Calculated in {(time()-start_time)} seconds.")

if __name__ == '__main__':
    main()