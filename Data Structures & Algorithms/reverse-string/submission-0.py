class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front = 0
        end = len(s) - 1
        for _ in range(len(s)//2):
            s[front], s[end] = s[end], s[front]
            front += 1
            end -= 1