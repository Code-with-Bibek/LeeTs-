class Solution:
    def plusOne(self, digits):
        n = len(digits)
        
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        
        # every digit was 9, so we need one more digit at the front
        return [1] + digits