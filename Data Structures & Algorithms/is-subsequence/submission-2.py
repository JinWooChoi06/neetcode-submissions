class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        scounts = {}
        tcounts = {}
        def count_letters(st: str, d: dict) -> None:
            for letter in st:
                if letter in d:
                    d[letter] += 1
                else:
                    d[letter] = 1
        count_letters(s, scounts)
        count_letters(t, tcounts)
        for letter in scounts.keys():
            if letter not in tcounts or scounts[letter] > tcounts[letter]:
                return False
        
        last_pos = -1
        for letter in s:
            try:
                last_pos = t.index(letter, last_pos + 1)
            except ValueError:
                return False
        return True