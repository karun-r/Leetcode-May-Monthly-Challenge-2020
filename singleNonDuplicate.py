#https://leetcode.com/problems/single-element-in-a-sorted-array/
def singleNonDuplicate(nums) -> int:

    lo, hi = 0, len(nums) - 1
        
    while lo < hi - 1:
        
        mid = (lo + (hi - lo)//2)
        isMidOdd  = mid % 2 == 0 # checks if mid point is causing a perfect split on the left branch
        areAdjNumbersMatching = nums[mid] == nums[mid+1] # checks if adjcent numbers are matching 
       
        if isMidOdd and not areAdjNumbersMatching: # perfect split on the left branch and adj numbers are not matching i.e. imbalance on right branch
            lo = mid
        elif isMidOdd and areAdjNumbersMatching: #perfect split on left branch and adj numbers are matching i.e. imbalance is on left branch 
            hi = mid
        elif not isMidOdd and not areAdjNumbersMatching: # not a perfect split, adj numbers are not matching i.e. imbalance is on left branch 
            hi = mid 
        elif isMidOdd and areAdjNumbersMatching: # not a perfect split, adj numbers are matching i.e. imbalance is on right branch 
            lo = mid
    if lo % 2 == 1:
        return nums[hi]
    elif lo % 2  == 0:
        return nums[lo]

print(singleNonDuplicate([3,3,7,7,10,11,11]))