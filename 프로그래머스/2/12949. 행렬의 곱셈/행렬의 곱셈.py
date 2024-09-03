def solution(arr1, arr2):
    answer = []
    
    for i, arr1_row in enumerate(arr1):
        result_row = []
        for j in range(len(arr2[0])):
            arr2_column = [t[j] for t in arr2]
            element = sum(([a * b for a, b in zip(arr1_row, arr2_column)]))
            result_row.append(element)
        answer.append(result_row)
        
    return answer