# 전공평점 = (학점 x 과목평점(letter)) 의 합 / 학점의 총합
score_basis = {  # 과목 평점
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

major_score = 0
score_grade_sum = 0
for _ in range(20):  # 과목, 학점, 레터그레이드 입력
    sbj, score_grade, letter_grade = input().split()
    score_grade = float(score_grade)
    if letter_grade == "P":
        continue

    major_score += score_grade * score_basis[letter_grade]
    score_grade_sum += score_grade

print('{:.6f}'.format(major_score / score_grade_sum))
