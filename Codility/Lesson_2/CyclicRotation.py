def solution(A, K):
    if len(A) == K:
        return A
    aux = []
    for i in range(len(A)):
        aux.append(A[(i - (K % len(A)))] )
    return aux