from collections import Counter


def migratoryBirds(arr):
    # Write your code here
    x = dict(Counter(arr))
    list_ = list(x.items())
    max_ = 0
    p = []
    for i in list_:
        if max_ < i[1]:
            max_ = i[1]

    for j in list_:
        if j[1] == max_:
            p.append(j[0])
    p.sort()

    maximum = max(x, key=x.get)
    return p[0]


if __name__ == '__main__':

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    print(result)
