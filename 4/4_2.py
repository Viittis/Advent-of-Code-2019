from time import time
# Validate pw against given rules

# 4.2// pw:ssä pitää aina olla lukupari, jos ei ole lukuparia, mutta esim. kolme peräkkäistä, niin ei lasketa.
def validate_pw(pw_in):
    pw_list = [x for x in str(pw_in)]

    pair_found = (any([pw_list[i],pw_list[i]] == pw_list[i:i+2] for i in range(len(pw_list) - 1)))

    if(pair_found):
        for i in range(1, len(pw_list)):
            if int(pw_list[i]) < int(pw_list[i - 1]):
                return False
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