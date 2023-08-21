class Queue:
    def __init__(self, max_size = -1):
        self.__queue = []
        self.__max_size = max_size

    def __repr__(self):
        return f'{self.__queue}'

    def is_empty(self):
        return self.__queue == []

    def size(self):
        return len(self.__queue)

    def enqueue(self, data):
        if self.is_full():
            return
        self.__queue.append(data)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.__queue.pop(0)

    def front(self):
        if self.is_empty():
            return None
        return self.__queue[0]
    
    def rear(self):
        if self.is_empty():
            return None
        return self.__queue[-1]
    
    def is_full(self):
        return self.size() == self.__max_size
    
    def clear(self):
        self.queue = []

# prof Nam's solution

def barista_coffee(order):
    Q_order = Queue()
    for o in order:
        Q_order.enqueue(o)
    barista_1 = 0
    barista_2 = 0
    customer_wait_longest_no = 0
    max_wait_time = 0
    already_coffee = []
    while not Q_order.is_empty():
        time_in, coffee_time, customer_no = Q_order.dequeue()
        customer_wait = 0
        if barista_1 > barista_2 and time_in < barista_1:
                barista_1, barista_2 = barista_2, barista_1
        if time_in < barista_1:
            customer_wait = barista_1 - time_in
        else:
            barista_1 = time_in
        
        if customer_wait > max_wait_time:
            max_wait_time = customer_wait
            customer_wait_longest_no = customer_no # memory customer who wait for longer number
        
        barista_1 += coffee_time # start Time begin make coffee to finish
        already_coffee.append([barista_1, customer_no])

    already_coffee.sort()
    [print(f'Time {c[0]} customer {c[1]} get coffee') for c in already_coffee]

    if max_wait_time == 0:
        print("No waiting")
    else:
        print(f"The customer who waited the longest is : {customer_wait_longest_no}")
        print(f"The customer waited for {max_wait_time} minutes")

print(" ***Cafe***")
log = [[int(c) for c in cafe.split(",")] + [i + 1] for i, cafe in enumerate(input("Log : ").split("/"))]
barista_coffee(log)