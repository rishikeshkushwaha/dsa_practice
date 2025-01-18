def mySqrt(x):

    if x == 0: return 0
    if x==1: return 1

    left = 1
    right = x//2

    while left <= right:
        mid = (left + right)//2

        if mid*mid <= x and (mid+1)*(mid+1) > x:
            return mid
        elif mid*mid < x:
            left = mid+1
        else: 
            right = mid -1 
    return -1


x = 100
print(mySqrt(x)) 


