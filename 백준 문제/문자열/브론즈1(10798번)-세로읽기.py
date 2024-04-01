array = []
max_len = 0
for _ in range(5):
    word = list(input())
    array.append(word)
    if len(word) > max_len:
        max_len = len(word)

for i in range(max_len):
    for j in range(5):
        try:
            print(array[j][i], end="")
        except IndexError:
            continue
