height, width = map(int, input().split())
chess = []
result = 10e5

for _ in range(height):
    chess.append(input())

black_board = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]

white_board = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]


def check(i, j):
    result_w = 0
    result_b = 0
    for di in range(8):
        for dj in range(8):
            ni, nj = i+di, j+dj
            if chess[ni][nj] != white_board[di][dj]:
                result_w += 1
            if chess[ni][nj] != black_board[di][dj]:
                result_b += 1

    return min(result_b, result_w)


for i in range(height-7):
    for j in range(width-7):
        result = min(result, check(i, j))

print(result)
