def solution(arr):
    low = arr[0]
    high = arr[0]
    low_count = 0
    high_count = 0
    for i in range(1,len(arr)):
        if arr[i] < low:
            low_count += 1
            low = arr[i]
        if arr[i] > high:
            high_count += 1
            high = arr[i]
    return [high_count, low_count]

if __name__ == "__main__":
    size = int(input())
    arr = [int(t) for t in input().strip().split()]
    ans = solution(arr)
    print(str(ans)[1:-1].replace(",",""))