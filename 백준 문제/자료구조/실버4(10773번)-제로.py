k = int(input())  # 100만의 input이므로 O(n)을 지켜야한다.
money = []

for _ in range(k):
    new_money = int(input())
    if new_money == 0:
        money.pop()
    else:
        money.append(new_money)

print(sum(money))
