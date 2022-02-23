def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    s1 = sum - arr[0]
    s2 = sum - arr[-1]
    print(f"{s2} {s1}")


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
