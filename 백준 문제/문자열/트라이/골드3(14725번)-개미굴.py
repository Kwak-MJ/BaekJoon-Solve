import sys

input = sys.stdin.readline


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, words: list):
        current_node = self.head

        for word in words:
            if word not in current_node.children:
                current_node.children[word] = Node(word)
            current_node = current_node.children[word]
        current_node.data = words

    def dfsPaint(self, current: Node, level: int):
        childrenList = list(current.children.keys())
        childrenList.sort()

        for children in childrenList:
            print("--" * level + children)
            self.dfsPaint(current.children[children], level + 1)


n = int(input())
t = Trie()
for _ in range(n):
    given = list(input().split())
    i = given[0]
    t.insert(given[1:])

t.dfsPaint(t.head, 0)
