# Input: {3, 4, -7, 3, 1, 3, 1, -4, -2, -2}
#
# Output: Subarray with zero - sum exists (return True/False)
#
# The
# subarrays
# with a sum of 0 are:
#
# {3, 4, -7}
# {4, -7, 3}
# {-7, 3, 1, 3}
# {3, 1, -4}
# {3, 1, 3, 1, -4, -2, -2}
# {3, 4, -7, 3, 1, 3, 1, -4, -2, -2}

class SubArrayWithZeroSum:

    def __init__(self, arr: [int]):
        self.arr = arr

    def has_zero_sum(self) -> bool:
        set_values: set = set()
        set_values.add(0)
        sum_result: int = 0
        for i in range(0, len(self.arr)):
            sum_result += self.arr[i]
            if set_values.__contains__(sum_result):
                return True
            set_values.add(sum_result)
        return False


test = SubArrayWithZeroSum([4, -6, 3, -1, 4, 2, 7])
print(test.has_zero_sum())
