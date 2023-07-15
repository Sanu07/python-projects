class WordBreak:

    def __init__(self, s, words):
        self.s = s
        self.words = words
        self.word_break(s, words)

    def word_break(self, s, words):
        result: bool = self.word_break_helper(s, words, 0)
        print(result)

    def word_break_helper(self, s, words, start) -> bool:

        if len(s) == start:
            return True

        for a in words:
            word_length: int = len(a)
            end: int = start + word_length
            if end > len(s) or len(s) == 0:
                continue

            if s[start:end] == a:
                if self.word_break_helper(s, words, end):
                    return True

        return False


word_break_result = WordBreak("leetcode", {"lee", "t", "code"})
