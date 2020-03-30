def countNumberOfOnes(n):

    ## reject non-negative integers
    if n <= 0:
        return -1
    
    ## keep a counter of number of 1s
    numOnes = 0

    for i in range(1, n + 1):
        for digit in str(i):
            if digit == '1':
                numOnes += 1
    
    return numOnes
