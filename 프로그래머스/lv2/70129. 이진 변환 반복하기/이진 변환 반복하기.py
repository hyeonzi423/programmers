def solution(s):
    cnt, zero = 0, 0
    while int(s) > 1:
        zero += s.count("0")
        s = str(bin(s.count("1"))[2:])
        cnt += 1
    answer = [cnt, zero]
    return answer