
#[5, 5, 2, 5, 5, 5, 5, 5, 5, 5]
def solution(arr, x):
    for i in range(len(arr)):
        a = arr[:i+1].count(x)
        b = len(arr[i+1:]) - arr[i+1:].count(x)
        if a == b:
            return i + 1

    return -1


test = [5, 5, 2, 3, 5, 1, 6]
print(solution(test, 5))