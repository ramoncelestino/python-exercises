def solution(A):
    s = sorted(A)
    s = list(filter(lambda x: x > 0, s))

    if(len(s) == 0):
        return 1

    if min(s) > 1:
        return 1
    for i in range(1, len(s)):
        if (s[i] - s[i - 1]) > 1:
            return s[i - 1] + 1
    return max(s) + 1