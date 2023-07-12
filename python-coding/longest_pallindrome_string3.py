class Longest_pallindrome_string:

    def longest_palindrome_string(self):
        str_1 = "dabcba"
        if len(str_1) == 0:
            print("")
            return
        if len(str_1) == 1:
            print(str_1)
            return

        longest = 0
        longest_str = None

        for s in range(0, len(str_1)):
            temp = self.helper(str_1, s, s)
            if len(temp) > longest:
                longest = len(temp)
                longest_str = temp

        print(longest_str)

    # noinspection PyMethodMayBeStatic
    def helper(self, str_1, begin, end):
        while begin >= 0 and end < len(str_1) and str_1[begin] == str_1[end]:
            begin -= 1
            end += 1
        return str_1[begin + 1: end]

    def __int__(self):
        pass


result = Longest_pallindrome_string()
result.longest_palindrome_string()
