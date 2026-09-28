class Solution:
    def isGood(self, nums):
        n = max(nums)
        if len(nums) != n + 1:
            return False
        
        for i in range(1, n):
            if nums.count(i) != 1:
                return False
        
        return nums.count(n) == 2