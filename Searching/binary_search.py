def bi_search(l, r, arr, target):
    if l <= r:
        mid = (l+r) // 2
        if target == arr[mid]:
            return True
        if arr[mid] < target:
            l = mid + 1
            bi_search(l, r, arr, target)    
        elif arr[mid] > target:
            r = mid - 1
            bi_search(l, r, arr, target)

    return False

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(arr)
print(k)
print(bi_search(0, len(arr) - 1, sorted(arr), k))