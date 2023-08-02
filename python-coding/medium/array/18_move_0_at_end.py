# Given an integer array, move all zeros present in it to the end. The solution should maintain
# the relative order of items in the array and should not use constant space.
#
# Input: {6, 0, 8, 2, 3, 0, 4, 0, 1}
#
# Output: {6, 8, 2, 3, 4, 1, 0, 0, 0}
#

def move_zeroes():
    arr_value: [int] = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    i = 0
    j = len(arr_value) - 1
    while i <= j:
        while arr_value[i] != 0:
            i += 1
        while not arr_value[j] > 0:
            j -= 1
        if i >= j:
            break
        temp: int = arr_value[i]
        arr_value[i] = arr_value[j]
        arr_value[j] = temp

    print(arr_value)


if __name__ == '__main__':
    move_zeroes()