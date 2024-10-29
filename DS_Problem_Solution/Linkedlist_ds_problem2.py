
# Here next question based on Dubly Linked List

class Node:
    def __init__(self, prev=None,item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self,start=None):
        self.start = start 

    def is_empty(self):
        return self.start == None
    
    def insert_at_start(self,data):
        n= Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n

    def insert_at_last(self,data):
        temp=self.start
        if self.start != None:
            while temp.next != None:
                temp = temp.next
            
        n=Node(temp,data,None)
        if temp == None:
            self.start=n
        else:
            temp.next=n

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next

    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None

    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None

    def delete_item(self,data):
            if self.start is None:
                pass
            else:
                temp=self.start
                while temp is not None:
                    if temp.item == data:
                        if temp.next is not None:
                            temp.next.prev=temp.prev
                        if temp.prev.next is not None:
                            temp.prev.next=temp.next    
                        else:
                             self.start=temp.next
                        break
                    temp.temp.next

    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self,start):
         self.current=start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current=self.current.next
        return data
    
    mydlsit=DLL()
    mydlsit.insert_at_start(10)
    mydlsit.insert_at_last(20)
    mydlsit.insert_after(mydlsit.search(10),15)
    for x in mydlsit:
        print(x, end=' ')
    print()


# Here correct version of upper code - Please check what is the issue in previous question .

class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class DLL:
    def __init__(self, start=None):
        self.start = start 

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.prev = n
        self.start = n

    def insert_at_last(self, data):
        n = Node(None, data, None)
        if self.is_empty():
            self.start = n
            return
        
        temp = self.start
        while temp.next is not None:
            temp = temp.next
            
        temp.next = n
        n.prev = temp

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = n
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()  # For a new line after printing the list

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.is_empty():
            return
        
        if self.start.next is None:  # Only one element
            self.start = None
            return
            
        temp = self.start
        while temp.next is not None:
            temp = temp.next
            
        # Now 'temp' is the last node
        temp.prev.next = None

    def delete_item(self, data):
        if self.is_empty():
            return
        
        temp = self.start
        while temp is not None:
            if temp.item == data:
                if temp.prev:  # Not the first node
                    temp.prev.next = temp.next
                else:  # First node case
                    self.start = temp.next
                
                if temp.next:  # Not the last node
                    temp.next.prev = temp.prev
                
                break  # Item found and deleted
            
            temp = temp.next

    def __iter__(self):
        return DLLIterator(self.start)
    
class DLLIterator:
    def __init__(self, start):
         self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data

# Usage example outside class definitions
mydlsit = DLL()
mydlsit.insert_at_start(10)
mydlsit.insert_at_last(20)
mydlsit.insert_after(mydlsit.search(10), 15)

# Print the list using the iterator
for x in mydlsit:
    print(x, end=' ')
print()   