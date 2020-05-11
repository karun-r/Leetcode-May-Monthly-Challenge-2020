#https://leetcode.com/problems/find-the-town-judge/
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        population = []
        trustees = {}
        if len(trust) == 0 and N == 1:
            return 1
        for n in trust:
            if n[0] not in trustees:
                trustees[n[0]] = -1
            else:
                trustees[n[0]] -= 1
            if n[1] not in trustees:
                trustees[n[1]] = 1
            else:
                trustees[n[1]] += 1
            
        judge = -1

        
        for trustee in trustees.keys():
            if trustees[trustee] == (N - 1):
                judge = trustee
        return judge
   
