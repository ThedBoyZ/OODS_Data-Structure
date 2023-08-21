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
        if self.isfull():
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

def barista_coffee(log):
    Q_time = Queue()
    Q_order = Queue()
    Q_wait = []  # This will store the waiting time for each customer
    Q1 = Queue()
    Q2 = Queue()
    state_time = 0
    state_time_2 = 0
    count_time = 0
    customer_no = 0
    wait = 0
    next_do = 0
    check = 0
    customer_numbers_q1 = []
    customer_numbers_q2 = []

    for order in log.split("/"):
        time, order_details = order.split(",")
        Q_time.enqueue(int(time))
        Q_order.enqueue(order_details)
        while not Q_order.is_empty():
            front,second = Q_time.second()
            if count_time < Q_time.front() and not (Q1.is_empty() and Q2.is_empty()):
                count_time += 1
                check += 1
                if check == 1:
                    next_do = 1
                    check = 2
            else:
                if Q1.is_empty() or Q2.is_empty():
                    Q_wait.append(wait)
                    wait = 0
                    Q_time.dequeue()
                    if Q1.is_empty():
                        item = Q_order.dequeue()
                        customer_no += 1
                        Q1.enqueue(int(item))
                        customer_numbers_q1.append(customer_no)
                    if Q2.is_empty() and Q_order.size() > 0:
                        item = Q_order.dequeue()
                        customer_no += 1
                        Q2.enqueue(int(item))
                        customer_numbers_q2.append(customer_no)
                else:
                    wait += 1
                    Q_wait[-1] = wait  # Update the waiting time for the last customer
                count_time += 1
            if front == second:
                print(f"{front} = {second}")
            if Q2.size() > 0:
                state_time_2 = int(Q2.front())
                state_time_2 -= 1
                Q2.dequeue()
                if state_time_2 - next_do == 0:
                    print(f"Time {count_time} customer {customer_numbers_q2.pop(0)} get coffee")
                    next_do = 0
                else:
                    Q2.enqueue(state_time_2)

            if Q1.size() > 0:
                state_time = int(Q1.front())
                state_time -= 1
                Q1.dequeue()
                if state_time == 0:
                    print(f"Time {count_time} customer {customer_numbers_q1.pop(0)} get coffee")
                else:
                    Q1.enqueue(state_time)

    max_value = max(Q_wait)
    max_index = Q_wait.index(max_value) + 1
    if max_value == 0:
        print("No waiting")
    else:
        print(f"The customer who waited the longest is: {max_index+1}")
        print(f"The customer waited for {max_value + 1} minutes")


print("***Cafe***")
print("Testcase student: #1/5")
print("Log: 0,3/0,7/2,3/7,7/10,5/10,1")
barista_coffee("0,3/0,7/2,3/7,7/10,5/10,1")

print("Testcase student: #2/5")
print("Log: 0,1/1,1/2,1/3,1/4,1/5,1")
barista_coffee("0,1/1,1/2,1/3,1/4,1/5,1")

print("Testcase student: #3/5")
print("Log: 0,1/0,1/1,1/1,1/2,1/2,1")
barista_coffee("0,1/0,1/1,1/1,1/2,1/2,1")
