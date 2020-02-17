# 퇴사 (14501번 문제)
N = int(input())
consult = [list(map(int, input().split())) for i in range(N)]
def max_pay(consult):
    m = consult[0][0]
    if m > len(consult):
        m = len(consult)
        consult[0][1] = 0
    if m == len(consult):
        if m == 1:
            return consult[0][1]
        max_value = 0
        max_value = max(max_pay(consult[i::]) for i in range(1, m))
        return max(max_value, consult[0][1])
    if m == 1:
        return (consult[0][1]+max_pay(consult[1::]))
    max_value = 0
    max_value = max(max_pay(consult[i::]) for i in range(1, m))
    return max(max_value, consult[0][1]+max_pay(consult[m::]))
print(max_pay(consult))