if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    arr.reverse()

    str_ = ""

    for i in arr:
        str_ += f"{i} "

    print(str_)
