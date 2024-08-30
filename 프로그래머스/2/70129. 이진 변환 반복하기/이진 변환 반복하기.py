def solution(s, arr=[0, 0]):
    if s == "1": return arr

    num_of_ones = s.count("1")
    num_of_zeros = len(s) - num_of_ones

    arr[0] += 1
    arr[1] += num_of_zeros
    
    s = f'{num_of_ones:b}'
    
    return solution(s, arr)