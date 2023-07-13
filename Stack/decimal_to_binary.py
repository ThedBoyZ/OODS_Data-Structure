class Stack:
    def __init__(self, list=None):
        if list is None:
            self.items = []
        else:
            self.items = list
        self.stack_size = len(self.items)

    def __repr__(self):
        return f'{self.items}'

    def push(self, value):
        self.items.append(value)
        self.stack_size += 1

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


def Decimal_to_binary(inp):
    decimal = int(inp)
    S1 = Stack()
    while decimal > 0:
        modulus = decimal%2
        decimal = decimal//2
        S1.push(modulus) 
    binary_str = ''.join(str(S1.pop()) for _ in range(S1.size()))
    print(f"Binary number : {binary_str}")

print(" ***Decimal to Binary use Stack***")
inp = input("Enter decimal number : ")
Decimal_to_binary(inp)