class Tree:
    def __init__(self, label, branches=()):
            self.label = label
            for branch in branches:
                assert isinstance(branch, Tree)
            self.branches = branches

    def __repr__(self):
        if self.branches:
            return 'Tree({0}, {1})'.format(self.label, repr(self.branches))
        else:
            return 'Tree({0})'.format(repr(self.label))

    def is_leaf(self):
        return not self.branches
    
    def get_height(self):
        if self.branches:
            return 1 + max([branch.get_height() for branch in self.branches])
        else:
            return 1

def fib_tree(n):
        if n == 1:
            return Tree(0)
        elif n == 2:
            return Tree(1)
        else:
            left = fib_tree(n-2)
            right = fib_tree(n-1)
            return Tree(left.label + right.label, (left, right))

def sum_labels(t):
    return t.label + sum([sum_labels(branch) for branch in t.branches])


fibonacci = fib_tree(5) # sums to 10
print(sum_labels(fibonacci))