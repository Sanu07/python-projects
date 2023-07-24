# Input: {4, 2, -3, -1, 0, 4}
#
# Subarrays
# with zero - sum are
#
# {-3, -1, 0, 4}
# {0}
#
# Input: {3, 4, -7, 3, 1, 3, 1, -4, -2, -2}
#
# Subarrays
# with zero - sum are
#
# {3, 4, -7}
# {4, -7, 3}
# {-7, 3, 1, 3}
# {3, 1, -4}
# {3, 1, 3, 1, -4, -2, -2}
# {3, 4, -7, 3, 1, 3, 1, -4, -2, -2}

class PrintSubArrayWithZeroSum(object):

    def __init__(self, arr: [int]):
        self.arr = arr

    def print_sub_array_with_zero_sum(self):
        map_value = {}
        set_value = set()
        arr = self.arr

        map_value[0] = [-1]
        set_value.add(0)
        sum_value = 0

        for i in range(0, len(arr)):
            sum_value += arr[i]

            if map_value.__contains__(sum_value):
                temp_list: [int] = map_value.get(sum_value)
                for n in temp_list:
                    print("[{0}...{1}]".format((n + 1), i))

            if not map_value.__contains__(sum_value):
                map_value.setdefault(sum_value, [])

            map_value.get(sum_value).append(i)


test = PrintSubArrayWithZeroSum([3, 4, -7, 3, 1, 3, 1, -4, -2, -2])
test.print_sub_array_with_zero_sum()
