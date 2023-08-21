def q_to_str(q):
    return ', '.join(q)  if q else "Empty"

def queue_sequnce(queue_word):
    queue = []
    dequeue = []
    for normal in queue_word:
        if normal.startswith('E'):
            queue.append(normal[2:])
            print(f"{', '.join(queue)}")
        elif normal.startswith('D'):
            if not queue:
                print("Empty")
                continue
            dequeue.append(queue.pop(0))
            print(f"{q_to_str(dequeue)} <- {q_to_str(queue)}")
    print(f"{q_to_str(dequeue)} : {q_to_str(queue)}")  

inp = input("Enter Input : ").split(",")
queue_sequnce(inp)


'''
def queue_sequnce(queue_word):
    queue = []
    dequeue = []
    for normal in queue_word:
        words = normal.split(",")
        for sub_word in words:
            sub_word = sub_word.strip()
            if sub_word.startswith('E'):
                value = sub_word[2:].strip()
                queue.append(value)
                print(f"{', '.join(queue)}")
            elif sub_word.startswith('D'):
                if len(queue) > 0:
                    front = queue.pop(0)
                    dequeue.append(front)
                    if len(queue) == 0: 
                        print(f"{front} <- Empty")  
                        print("Empty")                 
                    else:
                        print(f"{front} <- {', '.join(queue)}")
                    if len(dequeue) == 0:
                        print("Empty : Empty")  
                        break
                if len(dequeue) == 0:
                        print("Empty : Empty")                     

    if len(queue) > 0:
        print(f"{', '.join(dequeue)} : {', '.join(queue)}")
    elif len(queue) == 0 and len(dequeue) != 0:
        print(f"{', '.join(dequeue)} : Empty")
    else:
         print("Empty : Empty")     



inp = input("Enter Input : ").split(",")
queue_sequnce(inp)

'''