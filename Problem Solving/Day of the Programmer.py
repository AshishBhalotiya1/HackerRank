def dayOfProgrammer(y):
    # Write your code here
    count = 0
    if(y > 1918 and y <= 2700):
        if(y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)):
            count = 1
        if(count == 1):
            return('12.09.'+str(y))
        else:
            return('13.09.'+str(y))
    elif(y < 1918 and y >= 1700):
        if(y % 4 == 0):
            count = 1
        if(count == 1):
            return('12.09.'+str(y))
        else:
            return('13.09.'+str(y))
    elif(y == 1918):
        return('26.09.1918')


if __name__ == '__main__':

    year = int(input().strip())

    result = dayOfProgrammer(year)

    print(result + '\n')
