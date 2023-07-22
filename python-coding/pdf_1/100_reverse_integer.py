class ReverseInteger:

    def __init__(self):
        pass

    def reverse_integer(self):
        num = -123

        temp = abs(num)
        result = 0
        while temp != 0:
            rem = temp % 10
            result = result * 10 + rem
            temp //= 10
        print(result if num > 0 else -1 * result)


test = ReverseInteger()
test.reverse_integer()
