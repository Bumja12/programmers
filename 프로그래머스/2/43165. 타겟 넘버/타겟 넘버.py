def helper(arr, index, result, result_arr):
    if index == len(arr):
        result_arr.append(result)
        return
    
    helper(arr, index+1, result + arr[index], result_arr)
    helper(arr, index+1, result - arr[index], result_arr)

def solution(numbers, target):
    result_arr = []
    helper(numbers, 0, 0, result_arr)
    return result_arr.count(target)