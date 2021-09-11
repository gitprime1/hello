 def merge(A, l, h):
    sum = 0
    for i in range(l, h +1):
       sum += A[i]
    return sum
    def function(A: [], low, high):
        if low == high:
            return A[low]
        else:
            mid = (low + high) // 2
            return max(function(A, low, mid), function(A, mid + 1, high),merge(A,low,high)) 
n = int(input("the size of the array"))
optimus = []
i = 0
for i in range(n):
    z = int(input("enter the number"))
    optimus.append(z)
print(optimus)

print(function(optimus, 0, len(optimus) - 1))
