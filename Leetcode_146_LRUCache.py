class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(0,0), Node(0,0)
        self.cache = {}
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)
            if len(self.cache) > self.capacity:
                del self.cache[self.right.prev.key]
                self.remove(self.right.prev)
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.insert(node)


    def insert(self, node: Node):
        self.left.next.prev = node
        node.next = self.left.next
        self.left.next = node
        node.prev = self.left

    def remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)