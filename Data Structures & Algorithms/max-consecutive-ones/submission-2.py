class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxi = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter += 1
                maxi = max(maxi, counter)
            else:
                maxi = max(maxi, counter)
                counter = 0
        return maxi
        