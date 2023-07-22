class TwoSum:

    def __init__(self, numbers, target: int):
        self.numbers = numbers
        self.target = target

    def find_two_sum(self):
        map_val = {}
        for i in range(len(self.numbers)):
            if (self.target - self.numbers[i]) in map_val.keys():
                arr = [map_val.get(self.target - self.numbers[i]) + 1, i + 1]
                print(arr)
                return
            else:
                map_val[self.numbers[i]] = i


result = TwoSum([2, 7, 11, 15], 26)
result.find_two_sum()
