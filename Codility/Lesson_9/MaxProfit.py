
def solution(A):
    max_ending = max_slice = 0
    max_A = max(A)
    if max_A > 0:
        for i in range(len(A)):
            max_ending = max(0, max_ending + A[i])
            max_slice = max(max_slice, max_ending)
    else:
        max_slice = max_A
    return max_slice