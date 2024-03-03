import time
from random import random
import re
from TNode import TNode


class Treap:
    def __init__(self):
        self.root = None

    def Insert(self, key):
        print(f"Inserting {key}")
        new_node = TNode(key, random())
        self.root = self.TreapInsert(self.root, new_node)
        # print(f"Current tree:{self.__str__()}")

    def TreapInsert(self, node, new_node):
        if node is None:
            return new_node

        if new_node.key < node.key:
            node.left = self.TreapInsert(node.left, new_node)
            if node.left.priority > node.priority:
                node = self._RightRotate(node)
        else:
            node.right = self.TreapInsert(node.right, new_node)
            if node.right.priority > node.priority:
                node = self._LeftRotate(node)
        return node

    def TreapSearch(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self.TreapSearch(node.left, key)
        else:
            return self.TreapSearch(node.right, key)


    def _RightRotate(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        # Update parent pointers after rotation
        # left.parent = node.parent
        # if node.parent is not None:
        #     if node.parent.left == node:
        #         node.parent.left = left
        #     else:
        #         node.parent.right = left
        # node.parent = left
        return left

    def _LeftRotate(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        # Update parent pointers after rotation
        # right.parent = node.parent
        # if node.parent is not None:
        #     if node.parent.left == node:
        #         node.parent.left = right
        #     else:
        #         node.parent.right = right
        # node.parent = right
        return right

    def print_level_order(self):
        """Prints the tree elements in width-first order as a list"""
        if self.root is None:
            return []

        result = []
        queue = [self.root]
        current_level = 1
        next_level = 0

        while queue:
            node = queue.pop(0)
            result.append(node.key)
            current_level -= 1

            if node.left:
                queue.append(node.left)
                next_level += 1
            if node.right:
                queue.append(node.right)
                next_level += 1

            if current_level == 0:
                current_level = next_level
                next_level = 0

        return result


if __name__ == '__main__':
    treap = Treap()

    waitList= ['Z','Y','X','W','V','B','U','G','M','R','K','J','D','Q',
                'E','C','S','I','H','P','L','A','N','O','T','F']
    freq = {
        'A': 24, 'B': 7, 'C': 14,'D': 17, 'E': 26, 'F': 10, 'G': 8, 'H': 18, 'I': 22, 'J': 4,
        'K': 5, 'L': 16, 'M': 13, 'N': 19,'O': 23, 'P': 12, 'Q': 2, 'R': 20, 'S': 21, 'T': 25,
        'U': 15, 'V': 6, 'W': 11, 'X': 3, 'Y': 9,'Z': 1
    }

    for c in waitList:
        new_node = TNode(c, freq[c])
        treap.root = treap.TreapInsert(treap.root, new_node)

    print(f"Current tree:{treap.print_level_order()}")

    f = open("FellowshipOfTheRing.txt", "r")
    text = ""
    while True:
        c = f.read(1)
        if not c:
            break
        if re.match('^[a-zA-Z]+$', c):
            c = c.upper()
            text += c
    f.close()

    startTime = time.time()
    for i in range(10):
        for c in text:
            if not treap.TreapSearch(treap.root, c):
                print(f"Character {c} not found")
                break
    print("--- %s seconds ---" % (time.time() - startTime))
