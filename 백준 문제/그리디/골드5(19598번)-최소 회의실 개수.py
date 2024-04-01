'''
1. 아이디어
n = int(input()) 입력받기
time = [(시작1, 종료1), (시작2, 종료2), ...]으로 입력받기 O(N)
time을 시작 시간 기준 내림차순으로 정렬하기(종료 시간으로 정렬하면 언제 시작인지 알 수 없음)
end_time = [] 생성
count = 0 생성

(a) time에서 pop()을 통해 시작시간이 가장 작은 회의를 가져옴 O(1)

(b) end_time에 값이 존재하는 경우
    end_time의 0번째 인덱스 값과 비교해서 현재 start 시간이 더 크거나 같으면 heappop(0번째), heappush(현재 end) (count 변화 X)
    현재 start 시간이 더 작으면 현재 end 시간만 end_time에 heappush 시켜줌 (동시에 count += 1)

    end_time에 값이 존재하지 않는 경우
    heapq.heappush로 end_time에 종료시간 저장 (count += 1)

-----------------------------------------------
2. 시간 복잡도
* 백준 예외 -> 5배

2초 2000만 * 2

N = 10만
따라서 NlogN

time 리스트 입력 -> N
pop() 연산 -> O(1)
heapq 연산 -> logN
총 N번 수행 -> NlogN
-----------------------------------------------
3. 예외 case
* test case는 모두 통과함


'''
import heapq

n = int(input())
time = sorted([list(map(int, input().split()))
              for _ in range(n)], key=lambda x: x[0], reverse=True)

end_time = []
count = 0

while time:
    cur_start, cur_end = time.pop()

    if end_time:
        end_first = end_time[0]
        if end_first <= cur_start:
            heapq.heappop(end_time)
            heapq.heappush(end_time, cur_end)
        else:
            heapq.heappush(end_time, cur_end)
            count += 1
    else:
        heapq.heappush(end_time, cur_end)
        count += 1

print(count)
