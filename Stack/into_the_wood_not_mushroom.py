class Stack:
    def __init__(self, lst=None):
        if lst is None:
            self.items = []
        else:
            self.items = lst
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

def stack_sequence(string_woods):
    S1 = Stack()
    S2 = Stack()
    for word in string_woods:
        count = 0
        words = word.split(",")
        for sub_word in words:
            sub_word = sub_word.strip()

            if sub_word.startswith("A"):
                value = sub_word[2:].strip()
                S1.push(value)
                
            elif sub_word.startswith("B"):
                S2.items = S1.items[:] 
                # print(S2)
                most = 0
                i = 0
                while not S2.isEmpty():
                    brunch = S2.pop()
                    # print(f"b = {brunch}, m = {most}")
                    if i == 0:
                        count += 1 
                        most = int(brunch)
                    if int(brunch) > most:
                        count += 1    
                        most = int(brunch)                
                    i += 1
                print(count)

stack_type = input("Enter Input : ").split(",")
stack_sequence(stack_type)