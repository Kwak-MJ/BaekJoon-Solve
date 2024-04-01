left_money = int(input())

t_num = 0
f_num = 0
total_price = 2 * t_num + 5 * f_num


first_pos = left_money % 5

if left_money == 1 or left_money == 3:
    print(-1)
elif first_pos % 2 == 0:  # 짝수
    f_num = left_money // 5
    t_num = (left_money - 5*f_num) // 2
    print(f_num + t_num)
else:  # 홀수
    f_num = left_money // 5 - 1
    t_num = (left_money - 5*f_num) // 2
    print(f_num + t_num)
