class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = self.head
        self.length = 0
    
    def get(self, index: int) -> int:
        # Check for bounds
        if index >= self.length:
            return -1

        # Return ith index
        result = self.head.next

        for i in range(index):
            result = result.next

        return result.value

    def insertHead(self, val: int) -> None:
        self.head.next = Node(val, self.head.next)
        self.length += 1

        if self.tail == self.head:
            self.tail = self.head.next

    def insertTail(self, val: int) -> None:
        self.tail.next = Node(val)
        self.tail = self.tail.next

        self.length += 1

    def remove(self, index: int) -> bool:
        # Check for bounds
        if index >= self.length:
            return False

        pointer = self.head

        for i in range(index):
            pointer = pointer.next

        if self.tail == pointer.next:
            self.tail = pointer

        pointer.next = pointer.next.next
        self.length -= 1
        return True

    def getValues(self) -> List[int]:
        pointer = self.head.next
        result = []

        for i in range(self.length):
            result.append(pointer.value)
            pointer = pointer.next

        return result
