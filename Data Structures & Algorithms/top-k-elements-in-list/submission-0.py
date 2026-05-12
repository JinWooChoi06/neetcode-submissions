class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {}
        for num in nums:
            if num in numDict:
                numDict[num] += 1
            else:
                numDict[num] = 1

        ans = []
        sorted_dict = dict(sorted(numDict.items(), key=lambda item: item[1], reverse=True))
        keys = list(sorted_dict.keys())
        for i in range(k):
            ans.append(keys[i])
        return ans