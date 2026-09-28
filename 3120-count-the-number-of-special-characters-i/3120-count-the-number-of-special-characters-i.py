class Solution:
    def numberOfSpecialChars(self, word):
        seen = set(word)
        count = 0
        
        for c in "abcdefghijklmnopqrstuvwxyz":
            # special if both the small and capital version are in the word
            if c in seen and c.upper() in seen:
                count += 1
        
        return count