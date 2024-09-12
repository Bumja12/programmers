def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    dict1, dict2 = {}, {}
    
    for i in range(len(str1) - 1):
        word = str1[i:i+2]
        if word.isalpha():
            dict1[word] = dict1[word] + 1 if word in dict1 else 1
            
    for j in range(len(str2) - 1):
        word = str2[j:j+2]
        if word.isalpha():
            dict2[word] = dict2[word] + 1 if word in dict2 else 1
    
    intersection = 0
    for key in dict1:
        if key in dict2:
            intersection += min(dict1[key], dict2[key])
            
    union = sum([value for value in dict1.values()]) + sum([value for value in dict2.values()]) - intersection
    
    return 65536 * intersection // union if union else 65536
