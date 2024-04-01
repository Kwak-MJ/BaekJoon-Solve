'''
1. 아이디어
받는 돈 = 주려던 돈 - (등수 - 1)
따라서 손해가 적으려면 (이득이 많으려면) 돈을 원래 많이 주려던 사람이
앞 등수로 들어가야함

입력을 받고 정렬해서 순서대로 팁 계산
0이 나오는 순간부터 그 뒤는 계산 할 필요 없음

2. 시간 복잡도
2초 -> 2000만 * 2 지만, 백준에서 파이썬은 5배까지 가능
총 2억 연산

N = 10만이므로 총 NlogN 정도로 연산할 수 있음

sorted() 에서 NlogN
반복문에서 N
따라서 총 NlogN 만족
'''

N = int(input())

think = sorted([int(input()) for _ in range(N)], reverse=True)

total_tip = 0
for idx, tip in enumerate(think):
    if tip - idx <= 0:
        break

    total_tip += tip - idx

print(total_tip)
