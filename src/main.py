def function(A:[],low,right,p1,p2,m):
    key = str(low) + "," + str(right)
    if key in m: return m[key]
    if A == [low,right]:
        return 1
    if low > p1 or right > p2:
        return 0
    p = function(A,low + 1,right,p1,p2,m) + function(A,low,right + 1,p1,p2,m)
    m[key] = p
    return m[key]
n1 = int(input("enter the row number"))
n2 = int(input("enter the column number"))
m = {}
print(function([n1 - 1,n2 - 1],0,0,n1 - 1,n2 - 1,m))