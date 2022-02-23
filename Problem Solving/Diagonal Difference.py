import math

def diagonalDifference(arr):
    # Write your code here
    length = len(arr)
    row = int(math.sqrt(length))
    s1 =0
    for i in range(0, length, row+1):
        s1 += arr[i]
    s2= 0
    for i in range(row-1, length-row+1, row-1):
        s2 += arr[i]
    return f"{abs(s1-s2)}"
    

if __name__ == '__main__':
    
    n = int(input().strip())

    arr = []

    for _ in range(n):
        list_ = list(input().split())         
        arr = arr + list_
    for i in range(n*n):
        arr[i] = int(arr[i])
        
    result = diagonalDifference(arr)

    print(result)