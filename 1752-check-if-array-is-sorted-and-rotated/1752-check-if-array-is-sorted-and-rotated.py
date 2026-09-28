class Solution:
    def check(self, nums):
        n = len(nums)
        drops = 0
        
        for i in range(n):
            # compare with next element, last one wraps to the first
            if nums[i] > nums[(i+1) % n]:
                drops += 1
        
        return drops <= 1