# Input:
#
# nums = [8, 7, 2, 5, 3, 1]
# target = 10
#
# Output:
#
# Pair
# found(8, 2)
# or
# Pair
# found(7, 3)
#
# Input:
#
# nums = [5, 2, 6, 8, 1, 9]
# target = 12
#
# Output: Pair
# not found

class PairWithGivenSum:

    def __init__(self, arr, target: int):
        self.arr = arr
        self.target = target

    def find_pair(self):
        arr = self.arr
        target = self.target

        index_map = {}
        for i in range(0, len(arr)):
            if index_map.__contains__(target - arr[i]):
                return [arr[index_map.get(target - arr[i])], arr[i]]
            else:
                index_map[arr[i]] = i


test_given_sum = PairWithGivenSum([5, 2, 6, 8, 1, 9], 11)
print(test_given_sum.find_pair())
