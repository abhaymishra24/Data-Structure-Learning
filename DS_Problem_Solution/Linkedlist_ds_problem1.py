
# return a*b and f"this is double numbe{self.d}"

# Here is problem based on Linked list -

# Here first problem - 

# class Node:
#     def __init__(self, item=None,next=None):
#         self.item = item
#         self.next = next

# class SLL:

#     def __init__(self, start=None):
#         self.start= start

#     def is_empty(self):
#          return self.start== None
    
#     def insert_at_start(self, data):
#         n=Node(data,self.start)
#         self.start=n 
  
#     def insert_at_last(self,data):
#         n=Node(data)
#         if not self.is_empty():
#             temp=self.start
#             while temp.next is not None:
#                 temp=temp.next
#             temp.next=n
#         else:
#             self.start=n
            
#     def search(self,data):
#         temp =self.start
#         while temp is not None:
#             if temp.item==data:
#                 return temp 
#             temp= temp.next
#         return None
    
#     def insert_after(self,temp,data):
#         if temp is not None:
#             n=Node(data,temp.next)
#             temp.next=n

#     def print_list(self):
#         temp=self.start
#         while temp is not None:
#             print(temp.item, end=' ')
#             temp=temp.next

#     def delete_first(self):
#         if self.start is not None:
#             self.start=self.start.next

#     def delete_last(self):
#         if self.start is None:
#             pass
#         elif self.start.next is None:
#             self.start=None
#         else:
#             temp=self.start
#             while temp.next.next is not None:
#                 temp=temp.next
#             temp.next = None

#     def delete_item(self,data):
#         if self.start is None:
#             pass 
#         elif self.start.next is None:
#             if self.start.item==data:
#                 self.start=None
#         else:
#             temp=self.start
#             if temp.item==data:
#                 self.start=temp.next
#             else:
#                   while temp.next is not None:
#                       if temp.next.item==data:
#                           temp.next=temp.next.next
#                           break
#                       temp=temp.next

#     def __iter__(self):
#         return SLLIterable(self.start) 
    

# class SLLIterable:
#     def __init__(self,start):
#          self.current=start

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         data=self.current.next
#         return data
                

# mylist=SLL()
# mylist.insert_at_start(5)
# mylist.insert_at_start(3)
# mylist.insert_at_start(2)
# mylist.insert_at_start(1)
# mylist.insert_at_last(20)
# mylist.insert_after(mylist.search(3),4)
# mylist.print_list()
# mylist.delete_item(2)
# for x in mylist:
#     print(x,end=' ')


### [Leetcode Question] ###

# Here a Question base of Linked lis which is leetcode question-

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummyHead = ListNode(0)
#         tail = dummyHead
#         carry = 0

#         while l1 is not None or l2 is not None or carry != 0:
#             digit1 = l1.val if l1 is not None else 0
#             digit2 = l2.val if l2 is not None else 0

#             sum = digit1 + digit2 + carry
#             digit = sum % 10
#             carry = sum // 10

#             newNode = ListNode(digit)
#             tail.next = newNode
#             tail = tail.next

#             l1 = l1.next if l1 is not None else None
#             l2 = l2.next if l2 is not None else None

#         result = dummyHead.next
#         dummyHead.next = None
#         return result

# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         dummyHead = ListNode(0)
#         tail = dummyHead
#         carry = 0

#         while l1 is not None or l2 is not None or carry != 0:
#             digit1 = l1.val if l1 is not None else 0
#             digit2 = l2.val if l2 is not None else 0

#             total = digit1 + digit2 + carry  # Changed 'sum' to 'total'
#             digit = total % 10
#             carry = total // 10

#             newNode = ListNode(digit)
#             tail.next = newNode
#             tail = tail.next

#             l1 = l1.next if l1 is not None else None
#             l2 = l2.next if l2 is not None else None

#         return dummyHead.next  # No need to set dummyHead.next to None

# # Example usage (not part of the class)
# # You can create linked lists and test the function as follows:

# def print_linked_list(node: Optional[ListNode]):
#     while node:
#         print(node.val, end=' ')
#         node = node.next
#     print()

# # Creating two numbers represented by linked lists
# l1 = ListNode(2, ListNode(4, ListNode(3)))  # Represents number 342
# l2 = ListNode(5, ListNode(6, ListNode(4)))  # Represents number 465

# solution = Solution()
# result = solution.addTwoNumbers(l1, l2)

# # Print result linked


class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class SLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
        n = Node(data, self.start)
        self.start = n 
  
    def insert_at_last(self, data):
        n = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n
        else:
            self.start = n
            
    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp 
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
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

    def delete_last(self):
        if self.is_empty():
            return
        elif self.start.next is None:  # Only one element
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:  # Move to the second last node
                temp = temp.next
            temp.next = None  # Remove last node

    def delete_item(self, data):
        if self.is_empty():
            return
        
        # If the item to delete is at the start
        if self.start.item == data:
            self.start = self.start.next
            return
        
        # Iterate through the list to find the item to delete
        temp = self.start
        while temp.next is not None:
            if temp.next.item == data:
                temp.next = temp.next.next  # Bypass the node to delete it
                return
            temp = temp.next

    def __iter__(self):
        return SLLIterable(self.start) 
    

class SLLIterable:
    def __init__(self, start):
         self.current = start

    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item  # Return current item's value
        self.current = self.current.next  # Move to next node
        return data
                
# Example usage of SLL class
mylist = SLL()
mylist.insert_at_start(5)
mylist.insert_at_start(3)
mylist.insert_at_start(2)
mylist.insert_at_start(1)
mylist.insert_at_last(20)
mylist.insert_after(mylist.search(3), 4)

# Print the list using print_list method
mylist.print_list()  # Expected output: 1 2 3 4 5 20 

# Delete an item and print using iterator
mylist.delete_item(2)
for x in mylist:
    print(x, end=' ')  # Expected output: 1 3 4 5 20 
print()  # For a new line after printing the list from iterator.