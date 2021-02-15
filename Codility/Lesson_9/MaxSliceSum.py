


def solution(A):
    # write your code in Python 3.6
    max_ending = 0
    max_slice = min(A)

    min_value = min(A)

    for i in A:
        max_ending = max(i, max_ending + i)
        max_slice = max(max_ending, max_slice)

    return max_slice