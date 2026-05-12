class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        end1 = len(word1)
        end2 = len(word2)
        ans = ""
        while True:
            if i < end1 and j < end2:
                ans += word1[i]
                ans += word2[j]
                i += 1
                j += 1
            else:
                if i == end1:
                    ans += word2[j::]
                else:
                    ans += word1[i::]
                break
        return ans
