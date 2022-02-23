from collections import Counter


def sockMerchant(n, ar):
    # Write your code here
    count = dict(Counter(ar))
    # print(count)
    pairs = 0
    for key, value in count.items():
        x = value // 2
        pairs += x
    return pairs


if __name__ == '__main__':

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)
