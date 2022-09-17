from shutil import move
from turtle import st


def move_zeros(lst):
    
    new_list = [x for x in lst if not x == 0]
    new_list.extend([ x for x in lst if x == 0])
    
    return new_list



print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))