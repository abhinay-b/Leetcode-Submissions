from collections import defaultdict

class Node:    
        def __init__(self,key,val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None   

class LRUCache:  
    def __init__(self, capacity: int):
        self.head = Node(-1,-1)
        self.tail = self.head
        self.count = 0
        self.capacity = capacity
        self.dictn = defaultdict(Node)

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
        if key in self.dictn:
            self.dictn[key].val = value
            self.get(key)
            return
        node = Node(key,value)
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
            temp = self.tail
            self.tail = temp.prev
            self.dictn.pop(temp.key)
            self.tail.next = None
            temp.prev = None
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
