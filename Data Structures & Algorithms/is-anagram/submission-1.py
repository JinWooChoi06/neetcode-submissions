class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sd = {}
        td = {}
        for letter in s:
            if letter in sd:
                sd[letter] += 1
            else:
                sd[letter] = 1
        for letter in t:
            if letter in td:
                td[letter] += 1
            else:
                td[letter] = 1
        if sd == td:
            return True
        else:
            return False