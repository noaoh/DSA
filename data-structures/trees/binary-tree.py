class Node(object):
    def __init__(self,item,left=None,right=None,parent=None):
        self.value = item
        self.left = left
        self.right = right
        self.children = 0
        self.parent = parent
        self.temp = None

    def print(self):
        print("value = {0}".format(self.value))
        print("parent = {0}".format(self.parent))
        print("left child = {0}".format(self.left))
        print("right child = {0}".format(self.right))
        if self.left is not None:
            print("left child value = {0}".format(self.left.value))

        if self.right is not None:
            print("right child value = {0}".format(self.right.value))

        if self.parent is not None:
            print("parent value = {0}".format(self.parent.value))

        print("number of children = {0}".format(self.children))
        print("\n")

    def find_children(self,PRINT=False,RETURN=False):
        children = 0
        if self.left is not None:
            children += 1

        if self.right is not None:
            children += 1

        self.children = children

        if PRINT:
            print("number of children = {0}".format(self.children))
            print("\n")

        if RETURN:
            return children

class BinarySearchTree(object):
    def __init__(self,item=None):
        if item is not None:
            # Has a root, which points to the starting node
            # This node points to rest of the binary tree
            self.root = item
            self.size = None

        elif item is None:
            self.root = None
            self.size = None

        self.temp = None

    def print(self):
        if self.root is not None:
            print("root = {0}".format(self.root))
            print("root value = {0}".format(self.root.value))

            if self.root.left is not None:
                print("left child = {0}".format(self.root.left))
                print("left child value = {0}".format(self.root.left.value))

            if self.root.right is not None:
                print("right child = {0}".format(self.root.right))
                print("right child value = {0}".format(self.root.right.value))

        print("size = {0}".format(self.size))
        print("\n")

    def insert(self,parent,item):
        if parent is None:
            parent = item

        elif parent.value == item.value:
            parent.value = item.value

        elif item.value > parent.value:
            if parent.left is None:
                item.parent = parent
                parent.left = item

            elif parent.left is not None:
                self.insert(parent.left,item)

        elif item.value < parent.value:
            if parent.right is None:
                item.parent = parent
                parent.right = item

            elif parent.right is not None:
                self.insert(parent.right,item)

    def find_size(self,parent,PRINT=False):
        size = 0
        if parent is not None:
            size += 1
            size += self.find_size(parent.left)
            size += self.find_size(parent.right)

        self.size = size

        if PRINT:
            print("size of parent = {0}".size)

        return size

    def search(self,parent,value,PRINT=False):
        if parent is None:
            if PRINT:
                print("The value was not found!")
            return False

        elif parent.value < value:
            self.search(parent.left,value,PRINT)

        elif parent.value > value:
            self.search(parent.right,value,PRINT)

        elif parent.value == value:
            if PRINT:
                print("The value was found!")
                print("\n")
            return True

    def preorder_traversal(self,item,PRINT=False):
        path = []
        if item is not None:
            path.append(item.value)
            self.preorder_traversal(item.left)
            self.preorder_traversal(item.right)

        if PRINT:
            print("path = {0}".format(", ".join(str(e) for e in path)))

        return path

    def find_smallest(self,item,val=0,PRINT=False):
        if item is None:
            if PRINT:
                print("smallest value = {0}".format(val))
                print("\n")

            return val

        elif item.value < val:
            val = item.value
            self.find_smallest(item.right,val,PRINT)

        elif item.value == val or item.value > val:
            self.find_smallest(item.right,val,PRINT)

    def find_largest(self,item,val=0,PRINT=False):
        if item is None:
            if PRINT:
                print("largest value = {0}".format(val))
                print("\n")

            return val

        elif item.value > val:
            val = item.value
            self.find_largest(item.left,val,PRINT)

        elif item.value == val or item.value < val:
            self.find_largest(item.left,val,PRINT)

    def delete(self,item):
        children = item.find_children()
        if children == 0:
            item = None

        elif children == 1:
            if item.left is not None:
                item.value, item.left.value = item.left.value, item.value
                item.left = None

            elif item.right is not None:
                item.value, item.right.value = item.right.value, item.value
                item.right = None

        elif children == 2:
            print("not implemented yet")
            
oof = Node(5)
nani = Node(4)

doggo.left = oof
doggo.right = nani
doggo.find_children()
doggo.print()

shinderu = BinaryTree(Node(12))
shinderu.insert(shinderu.root,Node(1))
shinderu.insert(shinderu.root,Node(21))
wa = Node(2)
shinderu.insert(shinderu.root,wa)
shinderu.find_size(shinderu.root)
shinderu.print()

weeb = Node(2)
dweeb = Node(1)
scrub = Node(3)
omae = BinaryTree(weeb)
omae.insert(omae.root,dweeb)
omae.insert(omae.root,scrub)
omae.insert(omae.root,Node(21))
omae.insert(omae.root,Node(232))
omae.insert(omae.root,Node(12))
omae.find_size(omae.root)
omae.print()
omae.search(omae.root,232,PRINT=True)
omae.find_smallest(omae.root,val=omae.root.value,PRINT=True)
omae.find_largest(omae.root,val=omae.root.value,PRINT=True)

F = Node("F")
B = Node("B")
G = Node("G")
F.left = B
F.right = G

A = Node("A")
D = Node("D")
B.left = Node("A")
B.right = Node("D")

I = Node("I")
G.right = I

C = Node("C")
E = Node("E")
D.left = C
D.right = E

H = Node("H")
I.left = H

travesty = BinaryTree(F)
travesty.preorder_traversal(travesty.root,PRINT=True)
