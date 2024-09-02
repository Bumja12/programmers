def solution(brown, yellow):
    dimension = brown + yellow
    for i in range(3, int(dimension ** 0.5) + 1):
        if dimension % i == 0:
            inner_width = i - 2
            inner_height = (dimension // i) - 2
            if inner_width * inner_height == yellow:
                return sorted([inner_width+2, inner_height+2], reverse=True)
