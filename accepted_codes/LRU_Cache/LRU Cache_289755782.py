from collections import OrderedDict

class LRUCache:  
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictn = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.dictn:
            return -1
        self.dictn.move_to_end(key)
        return self.dictn[key]

    def put(self, key: int, value: int) -> None:
        self.dictn[key] = value
        self.dictn.move_to_end(key)
        if len(self.dictn) > self.capacity:
            self.dictn.popitem(last=False)
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
