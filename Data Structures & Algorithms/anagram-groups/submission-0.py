class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = []
        for word in strs:
            t = sorted(word)
            x = "".join(t)
            temp.append(x)
        sorte = set(temp)
        ans = []
        for sword in sorte:
            sub = []
            for word in strs:
                t = sorted(word)
                x = "".join(t)
                if sword == x:
                    sub.append(word)
            ans.append(sub)
        return ans

