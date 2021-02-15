def solution(N):
    sum = 0
    for i in range(1, N + 1):
        if (i * i) == N:
            sum += 1
        elif i * i > N:
            break
        else:
            if (N % i == 0):
                sum += 2

    return sum