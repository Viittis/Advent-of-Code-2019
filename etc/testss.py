
def test1():
    tlist = []
    tlist.append(["1","1","2","1","2","0"])
    tlist.append(["1","2","3","4","5","0"])

    for item in tlist:
        print(any([item[i],item[i]] == item[i:i+2] for i in range(len(item) - 1)))

def test2():
    tlist = 12687651123113132341142
    str_tlist = [x for x in str(tlist)]

    # Iteroidaan kirjain kerrallaan
    for i in range(len(str_tlist) - 1):
        # Tehdään kunnes breakataan
        while True:
            if str_tlist[i] == str_tlist[i+1]:
                i += 1
            else:
                break

test2()