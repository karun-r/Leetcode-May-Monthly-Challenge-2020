#https://leetcode.com/problems/valid-perfect-square/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 0:
            return False
        if num < 2:
            return True
        leftRange = 2
        rightRange = num // 2
        
        while leftRange <= rightRange:
            midPoint = leftRange + (rightRange - leftRange) // 2
            squareMid = midPoint * midPoint
            
            if squareMid == num:
                return True
            if squareMid < num:
                leftRange = midPoint + 1
            else:
                rightRange = midPoint - 1
             
        return False