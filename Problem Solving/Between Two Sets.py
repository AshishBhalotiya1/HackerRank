def getTotalX(a, b):
    # Write your code here
    ans = 0
    for i in range(1, 101):
        if all(i % x == 0 for x in a) and all(x % i == 0 for x in b):
            ans += 1
    return ans


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(total)
