
def get_sum(a,b):
    
    sorted_nums = sorted([a,b])

    result = [i for i in range(sorted_nums[0], sorted_nums[1]+1)]

    return sum(result)


