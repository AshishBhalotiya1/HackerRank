if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    # print(arr)

    max_ = -9 * 7
    for x in range(4):
        for y in range(4):
            p = []

            p.append((arr[y+1][x+1]))
            list_ = ((arr[y][x:x+3]) + p + (arr[y+2][x:x+3]))

            if sum(list_) > max_:
                max_ = sum(list_)

    print(max_)
