def pascals_triangle(n: int):
    pt = []
    for i in range(n):
        pt.append([0]*(i+1))
        pt[i][0] = 1
        for j in range(1, i):
            pt[i][j] = pt[i-1][j-1] + pt[i-1][j]
        pt[i][i] = 1
    return pt

print(pascals_triangle(6))
# prints [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
