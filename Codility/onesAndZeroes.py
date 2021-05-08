def solution(arr):
    res = [arr[0]]
    for i in range(1, len(arr)):
        print(i)
        res.append(arr[i] + res[i - 1])

    print(res)


test = [1, 0, 1, 1, 1, 0]
solution(test)