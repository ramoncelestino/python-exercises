def solution(A):
    # write your code in Python 3.6
    dictionary = {}
    for i in range(len(A)):
        if A[i] in dictionary:
            dictionary[A[i]] += 1
        else:
            dictionary[A[i]] = 1
    for i in dictionary.keys():
        if dictionary[i] % 2 != 0:
            return i
    return -1