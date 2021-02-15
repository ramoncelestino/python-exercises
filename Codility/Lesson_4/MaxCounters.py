def solution(N, A):
    res = [0] * N
    maxi = 0
    all_max = 0
    for i in range(len(A)):
        if A[i] > N:
            all_max = maxi
        if A[i] <= N:
            if res[A[i]- 1]  < all_max:
                res[A[i] - 1] = all_max + 1
            else:
                res[A[i] - 1] += 1
            if res[A[i] - 1] > maxi:
                maxi = res[A[i]- 1]

    for i in range(len(res)):
        if res[i] < all_max:
            res[i] = all_max

    return res