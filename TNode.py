class TNode:
    def __init__(self, key='', priority=0, parent=None, left=None, right=None):
        self.key = key
        self.priority = priority
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return f'(key={self.key}&priority={self.priority} left={self.left} right={self.right})'