''' file for the binary tree class

examples:
>>> t = BinaryTree(1)
>>> t2 = BinaryTree(5, BinaryTree(2), BinaryTree(7))
>>> t
BTree(1)
>>> t2
BTree(5, [BTree(2), BTree(7)])
>>> t2.insert(8)
"target label '8' successfully inserted"
>>> t2
BTree(5, [BTree(2), BTree(7, [None, BTree(8)])])
>>> t2.get_height()
3

'''

class BinaryTree:
    """ Binary Tree properties:
    search: O(log n)
    insertion: O(h), where h is the height of the tree. Worst case is O(n)
    """
    def __init__(self, label, left=None, right=None):
        self.label = label
        if right:
            assert isinstance(right, BinaryTree), "right child is not a binary tree but a {0}".format(type(right))
        if left:
            assert isinstance(left, BinaryTree), "left child is not a binary tree but a {0}".format(type(left))
        self.left = left
        self.right = right

    def __repr__(self):
        if self.right or self.left:
            return 'BTree({0}, [{1}, {2}])'.format(self.label, repr(self.left), repr(self.right))
        else:
            return 'BTree({0})'.format(self.label)

    def search(self, target_label):
        if target_label == self.label:
            return self.label
        elif target_label > self.label:
            return self.right.search(target_label)
        elif target_label < self.label:
            return self.left.search(target_label)
        return "target label '{0}' not found".format(target_label)

    def insert(self, target_label):
        if target_label > self.label:
            if not self.right:
                self.right = BinaryTree(target_label)
            else:
                return self.right.insert(target_label)
        elif target_label < self.label:
            if not self.left:
                self.left = BinaryTree(target_label)
            else:
                return self.right.insert(target_label)
        elif target_label == self.label:
            return "target label '{0}' already exists".format(target_label)
        return "target label '{0}' successfully inserted".format(target_label)
    
    def get_height(self):
        if self.left and self.right:
            return 1 + max([self.left.get_height(), self.right.get_height()])
        elif self.right:
            return 1 + self.right.get_height()
        elif self.left:
            return 1 + self.left.get_height()
        else:
            return 1

