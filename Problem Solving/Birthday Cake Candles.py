def birthdayCakeCandles(candles):
    # Write your code here
    a = max(candles)
    # print(a)
    return (candles.count(a))

if __name__ == '__main__':


    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    print(result)