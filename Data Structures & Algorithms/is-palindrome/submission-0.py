class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [char.lower() for char in s if char.isalnum()]
        front = 0
        end = len(new_s)-1
        for i in range(len(new_s)//2):
            if new_s[front] != new_s[end]:
                return False
            front += 1
            end -= 1
        return True