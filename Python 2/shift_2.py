def Rshift(num, shift):
    string_binary = ""

    def convert_to_binary(n):
        nonlocal string_binary

        if n >= 1:
            convert_to_binary(n // 2)
        if n // 2 != 0:
            string_binary = string_binary + str(n % 2)

    convert_to_binary(num)
    number = 0
    for i in range(len(string_binary)):
        if string_binary[len(string_binary) - 1 - i] == "1":  # Adjusted index calculation
            number += 2 ** i

    return number

n, s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n), int(s))) 