def weirdSubtract(n,k):
    array_index = list(str(n))
    array_index = [int(i) for i in array_index]
    summation = sum([int(i) for i in array_index])

    for i in range(k):
        if len(array_index) == 1 and array_index[-1] == 0:
            break
        if array_index[-1] > 0:
            array_index[-1] -= 1
        elif array_index[-1] == 0:
            if len(array_index) == 0:
                array_index[-1] = 0
            else:
                array_index.pop(-1)
                

    result = ''.join(str(digit) for digit in array_index)
    return result

n,s = input("Enter num and sub : ").split()

print(weirdSubtract(int(n),int(s)))