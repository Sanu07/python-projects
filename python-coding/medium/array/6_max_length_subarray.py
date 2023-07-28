# Given an integer array, find the maximum length subarray having a given sum
#
# nums[] = { 5, 6, -5, 5, 3, 5, 3, -2, 0 }
# target = 8
#
# Subarrays with sum 8 are
# {-5, 5, 3, 5}
# {3, 5}
# {5, 3}
#
# The longest subarray is { -5, 5, 3, 5 } having length 4
#

import numpy as np


def find_max_length_sub_array(arr_value: [int], sum_value: int) -> None:
    start = 0
    end = -1
    currSum = 0

    map_value = {}

    for i in range(0, len(arr_value)):

        currSum += arr_value[i]

        if currSum == sum_value:
            start = 0
            end = i
            break
        if map_value.__contains__(currSum - sum_value):
            start = map_value.get(currSum - sum_value) + 1
            end = i
            break
        else:
            map_value[currSum] = i

    if end == -1:
        print("No sub array")
    else:
        print(arr_value[start:end + 1])


if __name__ == '__main__':
    find_max_length_sub_array([5, 6, -5, 5, 3, 5, 3, -2, 0], sum_value=8)
