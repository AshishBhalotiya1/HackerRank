def kangaroo(x1, v1, x2, v2):
    # Write your code here
    distance = x1 - x2
    relative_speed = v1 - v2

    if relative_speed > 0 and distance % relative_speed == 0:
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result)
