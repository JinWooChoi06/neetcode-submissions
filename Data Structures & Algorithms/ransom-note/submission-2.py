class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen = {}
        maga = {}
        for letter in magazine:
            if letter not in seen.keys():
                seen[letter] = 1
            else:
                seen[letter] += 1
        for letter in ransomNote:
            if letter not in seen.keys():
                return False
            else:
                if letter not in maga.keys():
                    maga[letter] = 1
                else:
                    maga[letter] += 1
                if maga[letter] > seen[letter]:
                    return False
        return True
                