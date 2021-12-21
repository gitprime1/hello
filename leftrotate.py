def rotateLeft(d, arr):
    # Write your code here
    num = 0
    list1 = []
    num1 = len(arr)
    d = divmod(d,len(arr))[1]
    for i in range(1,d+1):
        if num != 0:
            arr = list1[:]
        list1 = arr[1:] + [arr[0]]
        num = num + 1
    return list1
print(rotateLeft(54,[1,2,3,4,5]))
print(rotateLeft(32,[9,5,4,3,2,1]))