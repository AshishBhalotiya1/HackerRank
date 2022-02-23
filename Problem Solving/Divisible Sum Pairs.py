def divisibleSumPairs(n, k, ar):
    # Write your code here
    count = 0
    for i in range(len(ar)):
        list_ = ar[:i]+ar[i+1:]
        for j in list_:
            if (ar[i] + j) % k == 0:
                count += 1
    return int(count/2)


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(result)
