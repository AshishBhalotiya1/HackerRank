def bonAppetit(bill, k, b):
    # Write your code here
    amount = sum(bill)
    Anna = int((amount - bill[k])/2)

    if Anna < b:
        print(b-Anna)
    elif Anna == b:
        print("Bon Appetit")


if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
