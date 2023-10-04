def bubble(l):
    for last in range(len(l)-1, 0, -1):
        swaped = False
        for i in range(last):
            if l[i] > l[i+1]:
                l[i], l[i+1] = l[i+1], l[i] #swap
                swaped = True
        if not swaped:
            break
l = [5,6,2,3,0,1,4]
bubble(l)
print(l)