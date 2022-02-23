def plusMinus(arr):
    # Write your code here
    length = len(arr)
    positive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    return (f'{positive/length}\n{negative/length}\n{zero/length}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = plusMinus(arr)

    print(result)
