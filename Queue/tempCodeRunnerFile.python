class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)
    
    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        return self.items.pop(0)

def wait_f_along(str):
    q_str = Queue()
    counter_1 = Queue()
    counter_2 = Queue()
    for word in str:
        q_str.enqueue(word)

    n1_limit = 3
    n2_limit = 2 
    count_n1 = 1
    count_n2 = 1
    for i in range(len(str)):
        if count_n1 > n1_limit:
            counter_1.dequeue()
            count_n1 = 1

        if count_n2 > n2_limit:
            counter_2.dequeue() 
            count_n2 = 1

        if counter_1.size() < 5:
            counter_1.enqueue(q_str.dequeue())
            count_n1+=1
            if counter_2.size() > 0:
                count_n2+=1
        else:
            counter_2.enqueue(q_str.dequeue())
            count_n2+=1
            count_n1+=1              
        print(f"{i+1} {q_str.items} {counter_1.items} {counter_2.items}")
        

inp = input("Enter people : ")
wait_f_along(inp)