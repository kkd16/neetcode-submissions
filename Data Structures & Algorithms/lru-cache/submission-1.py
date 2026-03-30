class LRUCache:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
    
    def __init__(self, capacity: int):
        self.max_capacity = capacity
        self.head = self.Node(None, None)
        self.tail = self.Node(None, None)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.cache_map = {}

    def _insert(self, node) -> None:
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node) -> None:
        prev_node = node.prev
        next_node = node.next
        
        prev_node.next = next_node
        next_node.prev = prev_node



    def get(self, key: int) -> int:

        if key in self.cache_map:
            node = self.cache_map[key]

            self._remove(node)
            self._insert(node)

            return node.val

        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache_map:
            node = self.cache_map[key]

            node.val = value

            self._remove(node)
            self._insert(node)

        else:
            new = self.Node(key, value)

            self.cache_map[key] = new
            
            self._insert(new)

            if len(self.cache_map) > self.max_capacity:
                del self.cache_map[self.tail.prev.key]

                self._remove(self.tail.prev)





        
            
        
