# Given a binary array, sort it in linear time and constant space. The output should print all zeroes, followed by all ones.
#
# Input: {1, 0, 1, 0, 1, 0, 0, 1}
#
# Output: {0, 0, 0, 0, 1, 1, 1, 1}
#

import array

class SortBinaryArray:

    def __init__(self):
        pass

    def swap_array_elem(self, arr: [int], i: int, j: int):
        temp: int = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def sort_binary_array(self) -> [int]:
        arr_value = array.array('I', [1, 0, 1, 0, 1, 0, 0, 1])

        i: int = 0
        j: int = 0
        while (i < len(arr_value)) and (j < len(arr_value)):
            while (i < len(arr_value)) and arr_value[i] != 1:
                i += 1
            while (j < len(arr_value)) and arr_value[j] != 0:
                j += 1
            if i >= len(arr_value) or j >= len(arr_value):
                break
            self.swap_array_elem(arr_value, i, j)
        return arr_value


test = SortBinaryArray()
print(test.sort_binary_array())
