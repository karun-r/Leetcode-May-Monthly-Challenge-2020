#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/534/week-1-may-1st-may-7th/3320/
class Solution:
    def firstUniqChar(self, s: str) -> int:
    
        i = -1 
        def getIndex(s:str) -> int:
            if len(s) == 0:
                return -1
            chr_list = []
            for i in range(0, len(s)):
                ch = s[i]
                
                if ch not in s[i+1:len(s)+1] and ch not in chr_list:
                    return i
                    break  
                chr_list.append(ch)
                
        j = getIndex(s)
        if j is not None:
            i = j
      
        return i
    
