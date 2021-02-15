def solution(A):
    # write your code in Python 3.6
    prefix_sum = [A[0]]
    for i in range(1, len(A)):
        prefix_sum.append(A[i] + prefix_sum[i - 1])

    min = 10000000
    for i in range(len(prefix_sum) - 1):
        count = abs(prefix_sum[-1] - (2 * (prefix_sum[i])))
        if min > count:
            min = count
    return min