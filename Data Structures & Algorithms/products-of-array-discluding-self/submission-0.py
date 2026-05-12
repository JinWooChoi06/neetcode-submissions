class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for num in nums:
            product *= num
        ans = []
        for num in nums:
            if num == 0:
                ans.append(self.redo(nums))
            else:
                ans.append(product//num)
        return ans
    def redo(self, nums: list[int]):
        index = nums.index(0)
        product = 1
        for i in range(len(nums)):
            if i != index:
                product *= nums[i]
        return product