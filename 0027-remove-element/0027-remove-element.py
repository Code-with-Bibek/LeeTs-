class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k = k + 1
        return k



s = Solution()

nums = [3, 2, 2, 3]
k = s.removeElement(nums, 3)
print("k =", k)              # 2
print("nums =", nums[:k])    # [2, 2]

nums = [0, 1, 2, 2, 3, 0, 4, 2]
k = s.removeElement(nums, 2)
print("k =", k)              # 5
print("nums =", nums[:k])    # [0, 1, 3, 0, 4]