def recursive_binary_strings(n, count ,current=""):
    if n < 0:
        print("Only Positive & Zero Number ! ! !")
        return False
    if n == 0:
        if count == 0:
            print("0")
        else:
            print(current)
    else:
        count+=1
        recursive_binary_strings(n - 1, count, current + "0")
        recursive_binary_strings(n - 1, count, current + "1")

inp = int(input("Enter Number : "))
recursive_binary_strings(inp,0,current="")