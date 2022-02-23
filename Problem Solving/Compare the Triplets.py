def compareTriplets(a, b):
    # Write your code here
    Alice = 0
    Bob = 0
    for i in range(3):
        if a[i] > b[i]:
            Alice += 1
        if a[i] < b[i]:
            Bob += 1
        if a[i] == b[i]:
            pass
    return f'{Alice}{Bob}'


if __name__ == '__main__':
    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
