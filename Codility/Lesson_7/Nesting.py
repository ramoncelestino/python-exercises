def solution(S):
    dictionary = {"]": "[", "}":"{", ")":"("}

    result = []
    for i in S:
        if (i == '[' or i == '{' or i == '('):
            result.append(i)
        else:
            if(len(result)) == 0:
                return 0

            if i in dictionary and dictionary[i] == result[-1]:
                result.pop()
            elif i in dictionary and dictionary[i] != result[-1]:
                return 0
    if len(result) > 0:
        return 0
    return 1