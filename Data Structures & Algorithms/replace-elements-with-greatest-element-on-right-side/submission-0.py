class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n):
            if i+1 == n:
                arr[-1] = -1
                return arr
            arr[i] = max(arr[i+1:])
