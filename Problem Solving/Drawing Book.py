def pageCount(n, p):
    # Write your code here

    # count from front
    if n % 2 == 1:
        n = n-1

    if p % 2 == 1:
        p = p-1

    front = int(p/2)
    back = int((n-p)/2)

    if front > back:
        return back
    else:
        return front


if __name__ == '__main__':

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    print(result)
