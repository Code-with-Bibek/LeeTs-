class Solution:
    def isPalindrome(self, x):

        number = str(x)

        reversed_number = number[::-1]

        if number == reversed_number:
            return True
        else:
            return False