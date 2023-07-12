class Reverse_polish_notation:

    def reverse_polish_notation(self, arr):
        operators = "+-*/"
        stack = []
        for s in arr:
            if s in operators:
                a = int(stack.pop())
                b = int(stack.pop())
                index = operators.index(s)
                match index:
                    case 0:
                        stack.append(a + b)
                    case 1:
                        stack.append(b - a)
                    case 2:
                        stack.append(a * b)
                    case 3:
                        stack.append(b / a)
            else:
                stack.append(s)

        print(stack.pop())

    def __int__(self):
        pass

    def main(self):
        # arr = ["2", "1", "+", "3", "*"]  # ((2 + 1) * 3) -> 9
        arr = ["4", "13", "5", "/", "+"]  # // (4 + (13 / 5)) -> 6
        self.reverse_polish_notation(arr)


result = Reverse_polish_notation()
result.main()
