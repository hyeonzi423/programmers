def solution(n,a,b):
    answer = 0
    if a > b:
        a, b = b, a
    while (a + 1 != b) or (a % 2 == 0):
        a = int((a + 1)/2)
        b = int((b + 1)/2)
        answer += 1
    return answer + 1