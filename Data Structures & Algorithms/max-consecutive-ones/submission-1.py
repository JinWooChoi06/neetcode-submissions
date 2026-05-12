class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max1 = 0
        for num in nums:
            if num == 1:
                count +=1
            else:
                if count > max1:
                    max1 =  count
                count = 0
        
        return max(max1, count)