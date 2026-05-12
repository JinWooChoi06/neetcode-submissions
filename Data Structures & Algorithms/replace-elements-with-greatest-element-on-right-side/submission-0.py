class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            maximum = 0
            if i == len(arr)-1:
                arr[i] = -1
                break
            for j in range(i + 1, len(arr)):
                if arr[j] > maximum:
                    maximum = arr[j]
            arr[i] = maximum
        return arr