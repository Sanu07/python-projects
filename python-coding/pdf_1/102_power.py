class CalculatePower:

    def __init__(self, num: int, power: int):
        self.num = num
        self.power = power

    def calculate_power(self):
        if self.num == 0:
            print(0)
            return

        if self.power == 0:
            print(1)
            return

        result: int = 1
        for i in range(1, self.power):
            result *= self.num

        print(result)


test_power = CalculatePower(3, 9)
test_power.calculate_power()
