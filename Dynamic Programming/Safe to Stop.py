import time
runway = [True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True,
        True, False, True, True, True, False, False, True, True, True, False, True, True, True
        ]
speed = 20

def safeToStop(runway, speed, position):
    if position>=len(runway) or position<0:
        return False
    
    if not runway[position]:
        return False

    if speed == 0:
        return True
    
    ans = False
    for newSpeed in [speed , speed - 1, speed + 1]:
        ans = ans or safeToStop(runway, newSpeed, position + newSpeed)
    
    return ans


def safeToStopMemo(runway, speed, position, memo):
    
    if memo == None:
        memo ={}
    
    if position in memo and speed in memo[position]:
        return memo[position][speed]
    

    if position>=len(runway) or position<0 or not runway[position] or speed<0:
        if position in memo:
            memo[position][speed] = False
            return False
        memo[position] = {speed : False}
        return memo[position][speed]

    if speed == 0:
        print (position,"("+str(speed)+")","->", end=" ")
        global stopAt 
        stopAt = position
        if position in memo:
            memo[position][speed] = True
            return True
        memo[position] = {speed : True}
        return memo[position][speed]
    
    for newSpeed in [speed - 1, speed , speed + 1]:
        if safeToStopMemo(runway, newSpeed, position + newSpeed, memo):
            print (position,"("+str(speed)+")", "->", end = " ")

            if position in memo:
                memo[position][speed] = True
                return True
            memo[position] = {speed : True}

            return True
    if position in memo:
        memo[position][speed] = False
        return False
    memo[position] = {speed : False}
    return memo[position][speed]

def findPath(memo, start):
    if start not in memo:
        return 
    for speed in memo[start]:
        if memo[start][speed] and speed!=0:
            print(start,"(speed = ", speed,")","<-", end=" ")
            findPath(memo, start - speed)


start_time = time.time()
memo = {}
stopAt = -1
print(safeToStopMemo(runway, speed, 0, memo))
print()
print(memo)
print()
findPath(memo, stopAt)
print()
