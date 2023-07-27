# Given an array containing only 0’s, 1’s, and 2’s, sort it in linear time and using constant space.
#
# Input: {0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0}
#
# Output: {0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2}

def swap(arr_value: [int], i: int, j: int):
    temp: int = arr_value[i]
    arr_value[i] = arr_value[j]
    arr_value[j] = temp


def sort_dutch_national_flag(arr_value: [int]) -> [int]:
    start = 0
    end = len(arr_value) - 1
    mid = 0
    pivot = 1

    while mid <= end:
        if arr_value[mid] < pivot:
            swap(arr_value, start, mid)
            mid += 1
            start += 1
        elif arr_value[mid] > pivot:
            swap(arr_value, mid, end)
            end -= 1
        else:
            mid += 1
    return arr_value


if __name__ == '__main__':
    nums = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]
    print(sort_dutch_national_flag(nums))
