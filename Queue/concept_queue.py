class Queue:
    def __init__(self):
        self.items = []

    def __repr__(self):
        return f'{self.items}'
      
    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

def concept_queue(str):
    Q1 = Queue()
    error_dq = 0
    error_input = 0
    mem = 0
    for normal in str:
        print(f"Step : {normal}")
        if normal.startswith("D"):
            clock_time = int(normal[1:])
            for i in range(clock_time):
                if Q1.size() == 0:
                    error_dq+=1
                elif Q1.size() != 0:
                    Q1.dequeue()
            print(f"Dequeue : {Q1}")
        elif normal.startswith("E"):
            clock_time = int(normal[1:])
            shift_clock = clock_time+mem
            for m in range(mem, shift_clock):
                Q1.enqueue(f"*{m}")
            mem = shift_clock
            print(f"Enqueue : {Q1}")
        else:
            error_input +=1
            print(f"{Q1}")
        print(f"Error Dequeue : {error_dq}")
        print(f"Error input : {error_input}")
        print(f"--------------------")
        

inp = input("input : ").split(",")
concept_queue(inp)