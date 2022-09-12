
def rgb(r, g ,b):

    hex_list = []
    rgb_list = [r,g,b]    

    length = len(rgb_list)

    rgb_list = lambda x: min(255, max(x, 0))

    for value in rgb_list:
        hex_list.append(hex(value).split('x')[1].upper())

    length = len(hex_list)
    
    for index in range(length):
        if hex_list[index].isdigit() and int(hex_list[index]) < 10:
            hex_list[index] = '0' + hex_list[index]


    result = ''.join(hex_list)
    return result


print(rgb(-20, 275, 125))