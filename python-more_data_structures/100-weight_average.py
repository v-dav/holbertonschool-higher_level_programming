#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0
    mul, sum_of_mul, sum_of_weights = 1, 0, 0
    for i in range(len(my_list)):
        for j in range(2):
            mul *= my_list[i][j]
            if j == 1:
                sum_of_weights += my_list[i][j]
        sum_of_mul += mul
        mul = 1
    return sum_of_mul / sum_of_weights
