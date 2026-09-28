class Solution:
    def maxDepth(self, s):
        depth = 0
        biggest = 0
        
        for ch in s:
            if ch == '(':
                depth += 1
                if depth > biggest:
                    biggest = depth
            elif ch == ')':
                depth -= 1
        
        return biggest