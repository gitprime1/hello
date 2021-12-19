
def function(A):
    greater_value = -999999999
    i, j, k, value = 0, 0, 0, 0
    for i in range(0, 4):
        for j in range(0, 4):
            value, value1 = 0, 0
            for k in range(j, j + 3):
                value = value + A[i][k] + A[i + 2][k]
            value1 = value + A[(i + i + 2) // 2][(j + j + 2) // 2]
            if value1 > greater_value:
                greater_value = value1
    return greater_value
print(function([[-9, -9, -9,  1, 1, 1],
 [0, -9,  0,  4, 3, 2],[-9, -9, -9,  1, 2, 3],
 [0, 0,  8,  6, 6, 0],
 [0,  0,  0, -2, 0, 0],
 [0, 0,  1,  2, 4, 0]]))
print(function([[1, 1, 1, 0, 0, 0],
[0, 1, 0, 0, 0, 0],
[1, 1, 1, 0, 0, 0],
[0, 0, 2, 4, 4, 0],
[0, 0, 0, 2, 0, 0],
[0, 0, 1, 2, 4, 0]]))

