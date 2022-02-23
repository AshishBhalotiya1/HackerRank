#
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def factorial(n):
    # Write your code here
    return (1 if n == 0 or n == 1 else n * factorial(n-1))


if __name__ == '__main__':

    n = int(input().strip())

    result = factorial(n)

    print(result)
