from collections import defaultdict


def printNodes(node):
    temp = node.next
    while temp:
        print(temp.val,temp.prev.val, '->', end=" ")
        temp = temp.next
class LRUCache: 
    
    class Node:    
        def __init__(self,val):
            self.val = val
            self.prev = None
            self.next = None   
            
    def __init__(self, capacity: int):
        self.head = self.Node(-1)
        self.tail = self.head
        self.count = 0
        self.capacity = capacity
        self.dictn = defaultdict(self.Node)

    def get(self, key: int) -> int:
        if key not in self.dictn:
            return -1
        curr = self.dictn[key]
        if curr != self.head.next:
            if curr == self.tail:
                self.tail = self.tail.prev
            prev = curr.prev
            nxt = curr.next
            prev.next = nxt
            if nxt:
                nxt.prev = prev
            curr.prev = self.head
            curr.next = self.head.next
            if self.head.next:
                self.head.next.prev = curr
            self.head.next = curr
            
        return curr.val

    def put(self, key: int, value: int) -> None:
        
        node = self.Node(key)
        node.prev = self.head
        node.next = self.head.next
        if self.head.next:
            self.head.next.prev = node
        self.head.next = node        
        self.dictn[key] = node
        
        if self.count < self.capacity:
            if self.count == 0:
                self.tail = node
            self.count += 1
        else:
            self.tail = self.tail.prev
            self.dictn.pop(self.tail.next.val)
            self.tail.next = None
        
        print('head,tail',self.head.next.val,self.tail.val)
        # printNodes(self.head)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
