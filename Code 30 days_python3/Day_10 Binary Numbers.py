def maximum_number_of_consecutive_1(N):
    x = str(bin(N))
    x = x[2:]
    max_count = 0
    count = 0
    for i in range(len(x)):
        if x[i] == '1':
            count += 1
        else:
            count = 0

        if count > max_count:
            max_count = count

    print(max_count)


if __name__ == '__main__':
    n = int(input().strip())
    maximum_number_of_consecutive_1(n)
