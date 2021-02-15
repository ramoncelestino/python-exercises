def solution(A):
    # write your code in Python 3.6
    A_filtered = filter(lambda x: x > 0, A)
    A_sorted = sorted(A_filtered)

    if min(A_sorted) > 1:
        return 0

    for i in range(1, len(A_sorted)):
        if (A_sorted[i] - A_sorted[i - 1]) != 1:
            return 0
    return 1