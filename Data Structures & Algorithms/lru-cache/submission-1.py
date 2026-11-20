class Node:
    def __init__(self, key:int, val:int=0, prev=None, next=None):
        self.key=key
        self.val=val
        self.prev=prev
        self.next=next

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity=capacity
        self.recent=Node(0,val=0)
        self.ago=Node(0,val=0)
        self.node_map={}
        self.recent.next=self.ago
        self.ago.prev=self.recent
    
    def remove(self, node: Node):
        node.next.prev=node.prev
        node.prev.next=node.next

    def insert(self, node: Node):
        self.recent.next.prev=node
        node.next=self.recent.next
        node.prev=self.recent
        self.recent.next=node

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node=self.node_map[key]
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node=self.node_map[key]
            node.val=value
            self.remove(node)
            self.insert(node)
        else:
            node=Node(key=key,val=value)
            self.insert(node)
            self.node_map[key]=node
            if len(self.node_map)>self.capacity:
                rem=self.ago.prev
                self.remove(rem)
                self.node_map.pop(rem.key)