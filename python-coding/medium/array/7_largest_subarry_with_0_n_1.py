# Given a binary array containing 0’s and 1’s, find the largest subarray with equal numbers of 0’s and 1’s.
#
# Input: {0, 0, 1, 0, 1, 0, 0}
#
# Output: Largest
# subarray is {0, 1, 0, 1} or {1, 0, 1, 0}
#

def largest_sub_array_with_0_n_1(arr):
    for i in range(0, len(arr)):
        if arr[i] == 0:
            arr[i] = -1

    curr_sum = 0
    end = -1
    max_value = 0

    map_value = {0: -1}

    for i in range(0, len(arr)):
        curr_sum += arr[i]

        if map_value.__contains__(curr_sum):
            if max_value < i - map_value[curr_sum]:
                max_value = i - map_value[curr_sum]
                end = i
        else:
            map_value[curr_sum] = i

    print("[{0}...{1}]".format((end - max_value + 1), end))


if __name__ == '__main__':
    largest_sub_array_with_0_n_1([0, 0, 1, 0, 1, 1, 0])
