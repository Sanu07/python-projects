class IsPalindrome:

    def __init__(self):
        pass

    def is_palindrome(self):
        num = 14456441
        temp = num
        result = 0
        while temp != 0:
            rem = temp % 10
            result = result * 10 + rem
            temp = temp // 10

        if result == num:
            print("Palindrome")
        else:
            print("Not Palindrome")


check = IsPalindrome()
check.is_palindrome()