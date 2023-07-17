class ReverseWord:

    def __init__(self):
        pass

    def reverse_word(self):
        s = "the sky is blue"
        words = s.split(" ")
        result = ""
        for word in reversed(words):
            result += word
            result += " "
        print(result[0:])


res = ReverseWord()
res.reverse_word()