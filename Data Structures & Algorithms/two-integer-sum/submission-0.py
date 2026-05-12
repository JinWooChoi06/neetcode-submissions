class Solution(object):
    def twoSum(self, nums, target):
        if not nums or "" in nums:
            return ""
        if len(nums) == 1 and target != nums[0]:
            return ""
        i = 0
        j = 0

        n = len(nums)
        for i in range(n):
             for j in range(n):
                if i == j:
                  j+=1
                if nums[i]+nums[j] == target:
                    return [i, j]
                    exit()
                else:
                     j+=1
                     
