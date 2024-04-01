from collections import deque

word = list(input())


def isPalindrome(word):
    word = deque(word)

    while len(word) > 1:
        if word.popleft() != word.pop():
            return False

    return True


if isPalindrome(word):
    print(1)
else:
    print(0)
