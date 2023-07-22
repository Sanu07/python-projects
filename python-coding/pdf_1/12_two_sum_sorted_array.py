from typing import List


class TwoSumSortedArray:

    def __init__(self):
        pass

    def get_index(self):
        arr = [2, 7, 11, 15]
        target = 26
        result: list[int] = self.find_index(arr, target)
        print(result)

    def find_index(self, arr, target) -> list[int]:
        i = 0
        j = len(arr) - 1
        while i <= j:
            sum = arr[i] + arr[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                result = [i + 1, j + 1]
                # print(result)
                return result


res = TwoSumSortedArray()
res.get_index()
