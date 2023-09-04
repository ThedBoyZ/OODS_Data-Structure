class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        final_string = ''
        current_node = self.head
        
        while current_node != None:
            # final_string += str(current_node.data)
            if current_node.next != None:
                final_string += str(current_node.data) + '->'
            if current_node.next == None:
                final_string += str(current_node.data)     
                
            current_node = current_node.next
        return final_string
    
    def search(self, target):
        found = False
        current_node = self.head
        
        while current_node != None and found != True:
            if current_node.data == target:
                found = True
                print("I found " + f'{current_node.data}' + " Already!")
                return 
                    
            current_node = current_node.next
        print("Target not found in the linked list.")
                
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        current_node = self.head
        
        while current_node.next != None:
            current_node = current_node.next
            
        current_node.next = new_node
        
    def delete_node(self, target):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.data == target:
            self.head = self.head.next
            return

        current_node = self.head
        while current_node.next != None:
            if current_node.next.data == target:
                current_node.next = current_node.next.next #shift it to the right is ""None""
                return
            current_node = current_node.next 
        
first_node = Node(1)
second_node = Node(2)
thrid_node = Node(3)

linked_list = LinkedList()
linked_list.head = first_node
linked_list.head.next = second_node
second_node.next = thrid_node

linked_list.search(2)
linked_list.insert(5)
linked_list.append(7)
linked_list.delete_node(5)
print(linked_list)

