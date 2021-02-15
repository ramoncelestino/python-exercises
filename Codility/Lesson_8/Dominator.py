def solution(A):
    # write your code in Python 3.6
    candidate = -1
    candidate_index = -1
    candidate_count = 0
    for i in range(len(A)):
        if candidate_count == 0:
            candidate = A[i]
            candidate_index = i
            candidate_count += 1
        else:
            if A[i] != candidate:
                candidate_count -= 1
            else:
                candidate_count += 1
    if A.count(candidate) > (len(A) // 2):
        return candidate_index
    return -1


