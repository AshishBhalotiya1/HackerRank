# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for _ in range(T):
    s = input()
    list_ = list(s)
    odd = ""
    even = ''
    for i in range(len(list_)):
        if i % 2 == 0:
            odd += list_[i]
        else:
            even += list_[i]
    print(f"{odd} {even}")
