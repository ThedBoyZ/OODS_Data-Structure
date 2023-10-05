def simple_sqrt(x):
    if x <= 1:
        return x
    left, right = 0,x
    result = 0
    
    while left <= right:
        mid = left + (right-left) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
        else:
            right = mid - 1
    if (left * left) - x < x - (right * right) :
        return left-1
    else:
        return right

x = int(input('simple sqrt: '))

result = simple_sqrt(x)
print(f"{result}")