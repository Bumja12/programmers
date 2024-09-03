def solution(arr1, arr2):
    arr2_transposed = list(zip(*arr2))
    
    return [[sum(a * b for a, b in zip(row1, col2)) for col2 in arr2_transposed] for row1 in arr1]
