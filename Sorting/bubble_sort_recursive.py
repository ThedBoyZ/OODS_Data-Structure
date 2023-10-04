def bubble_sort_recursive(l,n):
    if n == 1:
        return
    
    def bubble_pass(i):
        if i == n - 1:
            return
        
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1] , l[i] # swap two variable
        
        bubble_pass(i+1)
        
    bubble_pass(0)
    bubble_sort_recursive(l, n-1)

l = [int(x) for x in input("Enter Input : ").split()]
bubble_sort_recursive(l, len(l))
print(l)