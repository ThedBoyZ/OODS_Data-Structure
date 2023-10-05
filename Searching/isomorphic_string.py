def areIsomorphic(string1, string2):
    if len(string1) != len(string2):
        return False
    
    char_map1 = [-1] * 256
    char_map2 = [-1] * 256
    
    for i in range(len(string1)):
        char1, char2 = ord(string1[i]), ord(string2[i])
        
        if char_map1[char1] == -1 and char_map2[char2] == -1:
            char_map1[char1] = char2
            char_map2[char2] = char1
        elif char_map1[char1] != char2 or char_map2[char2] != char1:
            return False
    
    return True
s1,s2 = input("Enter str1,str2: ").split(",")
if areIsomorphic(s1,s2):
    print(f"{s1} and {s2} are Isomorphic")
else:
    print(f"{s1} and {s2} are not Isomorphic")    