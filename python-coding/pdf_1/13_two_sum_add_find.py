class TwoSumAddFind:

    arr: list[int] = []

    def __init__(self):
        pass

    def add(self, num: int):
        self.arr.append(num)

    def find(self, target: int):
        set_values: set = set()
        for num in self.arr:
            if set_values.__contains__(target - num):
                print(True)
                return
            else:
                set_values.add(num)

        print(False)


result = TwoSumAddFind()
result.add(2)
result.add(7)
result.add(11)
result.add(15)
result.find(10)
result.find(19)
