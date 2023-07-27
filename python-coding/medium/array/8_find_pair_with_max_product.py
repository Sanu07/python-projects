
# Given an integer array, find the maximum product of two integers in it.
#
# For example, consider array {-10, -3, 5, 6, -2}. The maximum product is the (-10, -3) or (5, 6) pair.
#

def find_pair(arr_value: [int]):
    largest: int = max(arr_value[0], arr_value[1])
    minimum: int = min(arr_value[0], arr_value[1])

    second_largest: int = minimum
    second_minimum: int = largest

    for i in range(2, len(arr_value)):
        second_largest = max(second_largest, min(largest, arr_value[i]))
        second_minimum = min(second_minimum, max(minimum, arr_value[i]))

        largest = max(largest, arr_value[i])
        minimum = min(minimum, arr_value[i])

    if largest * second_largest > minimum * second_minimum:
        return largest, second_largest
    else:
        return minimum, second_minimum


if __name__ == '__main__':
    nums = [-10, -3, 5, 6, -2]
    print(find_pair(nums))
