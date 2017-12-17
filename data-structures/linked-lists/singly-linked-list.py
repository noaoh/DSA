class Node(object):
    # initializes an object with a value and a "pointer" to another object with
    # a value (No object by default)
    def __init__(self,item):
            self.value = item
            self.next = None

    def print(self):
        print("Node")
        print("value = {0}".format(self.value))
        print("next node = {0}".format(self.next))
        if self.next is not None:
            print("next value = {0}".format(self.next.value))
        else:
            print("next value = None")
        print("\n")

# The linked list class is essentially an abstraction to manage multiple nodes
# The Node class can be used to create a linked list, but it's not a good idea
class SinglyLinkedList(object):
    def __init__(self, item=None):
        if item is not None:
            # Has a head, which points directly to the starting node
            self.head = item
            # Also has a tail, which  points to the rest of the nodes
            # Is set to None if there are no other nodes
            self.tail = item.next

        elif item is None:
            self.head = None
            self.tail = None

        self.length = 0

    def print(self):
        print("Singly Linked List")
        # head points directly to a node value's
        if self.head is not None:
            print("head = {0}".format(self.head))
            print("head value = {0}".format(self.head.value))
        else:
            print("head = None")

        if self.tail is not None:
            print("tail = {0}".format(self.tail))
            print("tail value = {0}".format(self.tail.value))
        else:
            print("tail = None")
        print("\n")

    # Takes O(n), where n is the number of nodes in the linked-list,
    # because it has to iterate through each node in the linked-list,
    # and each iteration is one operation
    # Returns the length of the linked list
    def get_length(self,PRINT=False):
        length = 0
        node = self.head
        # The last node is a None, and technically it isn't a node, so it doesn't
        # count.
        while node is not None:
            length += 1
            node = node.next

        if PRINT:
            print("length = {0}".format(length))

        self.length = length

    # Takes O(N) for reasons explained in the length function
    # Prints all values  in the linked list
    def print_all(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    # Takes O(N) for reasons explained in the length function
    # Gets the node at that position (not its value)
    def get_node(self,pos,PRINT=False):
        if pos < s
        n = 0
        node = self.head
        while n != pos:
            node = node.next
            n += 1

        if PRINT:
            print("node = {0}".format(node))

        return node

    # Takes O(N) for reasons explained in the length function
    # Get the value of the node at that position
    def get_value(self,pos,PRINT=False):
        node = get_node(self,pos,PRINT=False)
        if PRINT:
            print("node value = {0}".format(node.value))

        return node.value

    # Takes O(1) because it stops at the head, which means it only performs
    # one operation, which is swapping the values of head and the new value/item
    # Puts a node at the start of the linked list
    def prepend(self,val,PRINT=False,RETURN=False):
        head = self.head
        self.head, self.head.next = Node(val), head

        if PRINT:
            print("value {0} inserted at head".format(val))

        if RETURN:
            return head, val

    # Takes O(N) for reasons explained in the length function
    # Puts a node at the end of the linked list
    def append(self,val,PRINT=False,RETURN=False):
        n = 0
        node = self.head
        while n != self.get_length()-1:
            n += 1

        node.next = Node(val)
        if PRINT:
            print("value {0} inserted at end".format(val))

        if RETURN:
            return node.next, val

    # Takes O(pos) because it has to iterate through each node
    # until it reaches the position, which is each one operation
    # technically O(pos + 1) if you count the swap, but the +1 is
    # ignored in Big O notation, as it only looks at the greatest
    # value
    def insert(self,val,pos,PRINT=False,RETURN=False):
        n = 0
        if pos == 0:
            self.prepend(val,PRINT=False,RETURN=False)

        elif pos == self.get_length()-1:
            self.append(val,PRINT=False,RETURN=False)

        else:
            node = self.head
            while n != pos
                node = node.next
                n += 1

            node.next, node.next.next = Node(val), node.next
            node.value, node.next.value = node.next.value, node.value

            if PRINT:
                print("value {0} inserted at node {1}".format(node.value,pos))

            if RETURN:
                return pos, node.value



    # Takes O(pos) for reasons explained in the insert function
    # Removes the node at the pos
    def delete(self,pos,PRINT=False,RETURN=False):
        n = 0
        node = self.head
        print_pos = pos
        if pos+1 != self.length():
            while n != pos:
                node = node.next
                n += 1

            nani = node.value
            node.value, node.next.value = node.next.value, node.value
            node.next = node.next.next

        elif pos+1 == self.length():
            pos -= 1
            while n != pos:
                node = node.next
                n += 1

            nani = node.next.value
            node.next = None

        if PRINT:
            print("node at {0} of value {1} deleted".format(print_pos,nani))

        if RETURN:
            return pos, nani

    # Takes O(1) for reasons explained in the prepend function
    # Removes the first node in the linked list
    def shift(self,PRNT=False,RETRN=False):
        self.delete(0,PRINT=PRNT,RETURN=RETRN)

    # Takes O(N) for reasons explained in append function
    # Removes the last node in the linked List
    def pop(self,PRINT=False,RETURN=False):
        self.delete(self.length()-2,PRINT=PRNT,RETURN=RETRN)

print("Testing of the Node class")
cat = Node(3)
oof = Node(4)
nani = Node(5)
# cat should print its value, followed by None for next node and for next node value
cat.print()
cat.next = oof
# cat should print its value, followed by a memory address, and then the value of oof
cat.print()
oof.next = nani
# now oof has a next node
oof.print()

print("Testing of the SinglyLinkedList class")
omae = SinglyLinkedList()
# omae should print None for all values
omae.print()

shinderu = SinglyLinkedList(cat)
# shinderu should print the value of cat, followed by a memory address, and then the next value
shinderu.print()
# should print 3
print(shinderu.length())
print("\n")
# shinderu should print '(3 4 5)
shinderu.print_all()
# shinderu should print "value 6 inserted at node 2"
shinderu.insert(val=6,pos=2,PRINT=True)
# shinderu should print '(3 4 6 5)
shinderu.print_all()
