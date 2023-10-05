def bi_search(l,r,arr,x):
    if l == r:
        if arr[1] == x:
            return True
        else:
            return False
    elif l > r:
        return False
    
    a = arr[(l+r)//2]
    if a > x:
        return bi_search(l,(l+r)//2,arr,x)
    elif a < x:
        return bi_search(((l+r)//2)+1,r,arr,x)
    elif a == x:
        return True
    return False

inp = input('Enter Input : ').split('/')
arr,k = list(map(int,inp[0].split())),int(inp[1])
print(bi_search(0,len(arr)-1,sorted(arr),k))