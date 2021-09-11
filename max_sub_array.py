def merge(A:[],l,m,h):
    sum = 0
    left_sum = -1000000
    for i in range(m,l - 1,-1):
        sum = sum + A[i]
        if (sum > left_sum):
            left_sum = sum
    sm = 0
    right_sum = -100000
    for i in range(m + 1,h + 1):
        sm += A[i]
        if sm > right_sum:
            right_sum = sm
    return left_sum + right_sum

def function(A:[],low,high):
    if low == high:
        return A[low]
    else:
      mid = (low + high) // 2

      return max(function(A,low,mid),function(A,mid + 1,high),merge(A,low,mid,high))


n = int(input("the size of the array"))
optimus = []
i = 0
for i in range(n):
    z = int(input("enter the number"))
    optimus.append(z)
print(optimus)

print(function(optimus, 0, len(optimus) - 1))
