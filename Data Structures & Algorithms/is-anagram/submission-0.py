class Solution:
    def isAnagram(self, s, t):
        sorts = ''.join(sorted(s))
        sortt = ''.join(sorted(t))
        if sorts == sortt:
            return True
        return False
        
