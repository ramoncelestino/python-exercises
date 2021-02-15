def solution(A):
    # write your code in Python 3.6
    s = list(map(lambda x: abs(x), A))
    return len(set(s))