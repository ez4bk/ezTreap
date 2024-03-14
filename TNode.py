class TNode:
    def __init__(self, key='', priority=0, parent=None, left=None, right=None):
        self.key = key
        self.priority = priority
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return (f'(key={self.key} '
                # f'priority={self.priority} '
                f'parent={self.parent.key if self.parent else None} '
                f'left={self.left.key if self.left else None} '
                f'right={self.right.key if self.right else None})')