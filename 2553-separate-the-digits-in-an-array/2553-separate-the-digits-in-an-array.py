class Solution:
    def separateDigits(self, nums):
        answer = []
        
        for number in nums:
            for digit in str(number):
                answer.append(int(digit))
        
        return answer