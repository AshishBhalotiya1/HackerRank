def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_count = 0
    for i in apples:
        if i + a >= s and i + a <= t:
            apple_count += 1

    orange_count = 0
    for i in oranges:
        if b + i >= s and b + i <= t:
            orange_count += 1
    return (str(apple_count) + "\n" + str(orange_count))


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    result = countApplesAndOranges(s, t, a, b, apples, oranges)

    print(result)
