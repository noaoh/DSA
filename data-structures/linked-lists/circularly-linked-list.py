class Node(object):
    def __init__(self,item):
        self.value = item
        self.next = None
        self.prev = None

    def print(self):
        print("previous node = {0}".format(self.prev))
        if self.prev is not None:
            print("previous value = {0}".format(self.prev.value))
        else:
            print("previous value = None")

        print("current node")
        print("value = {0}".format(self.value))


        print("next node = {0}".format(self.next))
        if self.next is not None:
            print("next value = {0}".format(self.next.value))
        else:
            print("next value = None")

        print("\n")

class CircularlyLinkedList(object):
    def __init__(self, item=None):
        if item is not None and item.next is not None:
            self.head = item
            self.tail = item.next
            self.end = item.next

        elif item is None:
            self.head = None
            self.tail = None

        self.median_idx = 0
        self.length = 0

    def get_length(self,PRINT=False):
        length = 0
        node = self.head

        while node is not None:
            length += 1
            node = node.next

        if PRINT:
            print("length = {0}".format(length))

        self.length = length
        return self.length

    def print_all(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def get_median_idx(self):
        self.median = int((self.get_length()-1)/2)
        return self.median

    def get_node(self,pos,PRINT=False):
        if pos <= self.get_median_idx():
            n = 0
            node = self.head

            while n != pos:
                node = node.next
                n += 1

        elif pos > self.get_median_idx():
            n = self.get_length() - 1
            node = self.end

            while n != pos:
                node = node.prev
                n -= 1

        if PRINT:
            print("node = {0}".format(node))

        return node

    def get_node_value(self,pos,PRINT=False):
        node = self.get_node(pos)

        if PRINT:
            print("node value = {0}".format(node.value))

        return node.value

    def prepend(self,val,PRINT=False,RETURN=False):
        old_head = self.head
        head = Node(val)
        self.head, self.head.next = head, old_head
        old_head.prev = head
        head.prev = self.end

        self.length += 1

        if PRINT:
            print("value {0} inserted at head".format(val))

        if RETURN:
            return self.head, val

    def append(self,val,PRINT=False,RETURN=False):
        old_end = self.end
        end = Node(val)
        self.end.prev, self.end = old_end, end
        old_end.next = end
        end.next = self.head

        self.length += 1

        if PRINT:
            print("value {0} inserted at end".format(val))

        if RETURN:
            return self.end, val

    def insert(self,val,pos,PRINT=False,RETURN=False):
        if pos == 0:
            self.prepend(val,PRINT=False,RETURN=False)

        elif pos == self.length()-1:
            self.append(val,PRINT=False,RETURN=False)

        else:
            node = get_node(pos)
            new_node = Node(val)
            node.next, node.next.next = new_node, node.next
            node.value, new_node.value = new_node.value, node.value

            new_node.next.prev, node.next.next.prev = node, node.next

            self.length += 1

            if PRINT:
                print("value {0} inserted at node {1}".format(node.value,pos))

            if RETURN:
                return pos, node.value
