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
    


def color_rush(play):
    # play = play[::-1]
    S1 = Stack()
    S2 = Stack()
    S3 = Stack()
    combo = 0

    for i in range(len(play)):
        if i % 3 == 0:
            S1.push(play[i])
        elif i % 3 == 1:
            S2.push(play[i])
        elif i % 3 == 2:
            S3.push(play[i])
    # checj if they have same top
    # if so pop all from every stack
        # print(S1.peek(),S2.peek(),S3.peek())
        if S1.peek() == S2.peek() == S3.peek():
            sub_1 = S1.pop()
            sub_2 = S2.pop()
            sub_3 = S3.pop()
            combo+=1


    keep_list = []
    sorted_stack = sorted([S1,S2,S3], key=lambda x:x.size())
    most_size_stack = sorted_stack[-1]
    if S1.size() == S2.size() == S3.size():
        i = 0
    elif S1.size() == S2.size():
        i = 1
    elif most_size_stack == S1:
        i = 2
    elif most_size_stack == S2:
        i = 1
    elif most_size_stack == S3:
        i = 0

    while not (S1.isEmpty() and S2.isEmpty() and S3.isEmpty()):
        
        # print(S1.peek(),S2.peek(),S3.peek())
        if i % 3 == 0 and not S3.isEmpty():
            keep_list.append(S3.pop())
        elif i % 3 == 1 and not S2.isEmpty():
            keep_list.append(S2.pop())
        elif i % 3 == 2 and not S1.isEmpty():
            keep_list.append(S1.pop())
        i+=1
    print(len(keep_list))
    if len(keep_list) == 0:
        print("Empty")
    else:
        print("".join(keep_list))
    
    if combo > 1:
        print(f"Combo : {combo} ! ! !")
        



inp = input('Enter Input : ').split()
color_rush(inp)