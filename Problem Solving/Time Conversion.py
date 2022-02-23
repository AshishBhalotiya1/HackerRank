def timeConversion(s):
    # Write your code here
    if s[8] == 'A':
        if s[0] == "1" and s[1] == "2":
            s[0] = "0"
            s[1] = "0"
    elif s[8] == 'P':
        if s[0] == "1" and s[1] == "2":
            pass
        else:
            hr = int(s[0]+s[1])
            hr = 12 + hr
            hr = list(str(hr))
            s[0] = hr[0]
            s[1] = hr[1]
    s.pop()
    s.pop()
    time = ""
    for i in s:
        time += i
    return(time)


if __name__ == '__main__':

    s = list(input())

    result = timeConversion(s)

    print(result)
