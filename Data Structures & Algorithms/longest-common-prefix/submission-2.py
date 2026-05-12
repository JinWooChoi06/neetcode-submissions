class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        temp = ""
        for word in strs:
            temp = ""
            if not ans:
                ans = word
                # If the first word is empty, we must handle it to ensure ans isn't overwritten later
                if not ans: return ""
                continue
            for i in range(len(word)):
                if i > len(ans)-1:
                    break
                if word[i] == ans[i]:
                    temp += word[i]
                else:
                    break
            ans = temp
            if not ans: return ""
        return ans