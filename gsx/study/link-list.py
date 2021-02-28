class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def add_node(self, node):
        if not self.head:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def get(self, index):
        if not self.head:
            print('不存在')
            return None
        cur = self.head
        for i in range(index):
            if i < index and not cur.next:
                print('不存在')
                return None
            cur = cur.next
        print(cur.value)
        return cur

    def traverse(self):
        cur = self.head
        while cur.next:
            print(cur.value)
            cur = cur.next
        print(cur.value)

    def is_ring(self, linked_list):

        if not linked_list.head:
            return False

        pointer1 = pointer2 = linked_list.head

        while pointer2 and pointer2.next:
            pointer1 = pointer1.next
            pointer2 = pointer2.next.next

            if pointer1 == pointer2:
                pointer3 = linked_list.head
                step = 0
                while pointer3 != pointer2:
                    step += 1
                    pointer3 = pointer3.next
                    pointer2 = pointer2.next

                print(pointer3.value)
                return step
        return False




linked_list1 = LinkedList()

linked_list1.add(1)
linked_list1.add(2)
linked_list1.add(3)
linked_list1.add(4)
linked_list1.add(5)
linked_list1.add(6)
linked_list1.add(7)
linked_list1.add(8)
linked_list1.add(9)
linked_list1.add(10)

linked_list1.add_node(linked_list1.get(10))

print(linked_list1.is_ring(linked_list1))

# linked_list1.traverse()




