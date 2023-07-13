def mod_position(arr, s):
    array_string = list(str(arr))
    array_keepword = []
    for i in range(len(array_string)):
        if (i+1) % s == 0:
            array_keepword.append(array_string[i])
    return array_keepword

print("*** Mod Position ***")

arr,s = input("Enter Input : ").split(",")

print(mod_position(str(arr),int(s)))