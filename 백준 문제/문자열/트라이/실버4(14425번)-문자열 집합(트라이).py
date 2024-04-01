class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        current_node = self.head

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = Node(char)
            current_node = current_node.children[char]
        current_node.data = word

    def search(self, word):
        current_node = self.head

        for char in word:
            if char not in current_node.children:
                return False
            else:
                current_node = current_node.children[char]

        if current_node.data == word:
            return True
        else:
            return False

    def starts_with(self, prefix):
        current_node = self.head
        result = []

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None  # prefix 를 만족하는 애도 없으면 시작하는 단어가 있을 수가 없음

        current_node = [current_node]
        next_node = []  # next_node는 임시용도, current로 다 업데이트
        while True:
            for node in current_node:  # 리스트에 append하고 for문 하는건 큐와 비슷한 역할
                if node.data:
                    result.append(node.data)
                next_node += list(node.children.values())

            if len(next_node) != 0:
                current_node = next_node
                next_node = []
            else:
                break

        return result


trie = Trie()
n, m = map(int, input().split())
for _ in range(n):
    trie.insert(input())

count = 0
for _ in range(m):
    if trie.search(input()):
        count += 1

print(count)
