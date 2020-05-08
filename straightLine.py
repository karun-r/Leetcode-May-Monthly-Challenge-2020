#https://leetcode.com/explore/challenge/card/may-leetcoding-challenge/535/week-2-may-8th-may-14th/3323/
def checkStraightLine(coordinates):
    def getSlope(a,b):
        # a : (x1,y1) , b : (x2, y2)
        rise = b[1] - a[1]
        run  = b[0] - a[0]
        try:
            slope = rise/run
        except ZeroDivisionError:
            slope = None        
        return slope
    numCord = len(coordinates)
    if numCord == 1 or numCord == 2:
        return True
    firstTwoPoints = coordinates[:2]
    initialSlope = getSlope(firstTwoPoints[0],firstTwoPoints[1])
    isLine = True
    referencePoint = firstTwoPoints[1]
    for point in coordinates[2:]:
        if initialSlope != getSlope(referencePoint, point):
            return False
        else:
            referencePoint = point
    return isLine
    
print(checkStraightLine([[-1,1],[-6,-4],[-6,2],[2,0],[-1,-2],[0,-4]]))
