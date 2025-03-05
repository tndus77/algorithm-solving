def solution(clothes):
    answer = 1
    dict_clothes = {}
    
    # 종류: [값]
    for value, key in clothes:
        if key in dict_clothes:
            dict_clothes[key] += [value]
        else:
            dict_clothes[key] = [value]
    
    for _, value in dict_clothes.items():
        answer *= (len(value) + 1)
    return answer - 1