def stanton_measure(arr):
    
    stanton = arr.count(arr.count(1))
    
    return stanton


print(stanton_measure([1, 4, 3, 2, 1, 2, 3, 2]))