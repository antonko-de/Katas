def in_array(array1, array2):
    
    new_arr = []

    for item in array1:

        for i in array2:
            if item in i and not item in new_arr:
                new_arr.append(item)

    return new_arr


print(in_array(["arp", "live", "strong"], ["lively", "alive", "harp", "sharp", "armstrong"]))