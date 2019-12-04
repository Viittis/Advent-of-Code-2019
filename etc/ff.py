def remove_duplicates(data_in):
    uniques = set(data_in[0])
    uniques.update(data_in[1])

    print(uniques)

    duplicates = []

    for list in data_in:
        for coords in list:
            if coords not in uniques:
                duplicates.append(coords)

    return duplicates

arr = [(1,2),(3,4)]
arr.append([(4,5),(5,6),(1,2)])

test = remove_duplicates(arr)

print(test)