# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
dict_ = {}
for _ in range(n):
    name, phone = input().split()
    dict_[name] = phone
try:
    while True:
        name_ = input()
        if name_ != "":
            if name_ in dict_:
                print(f"{name_}={dict_[name_]}")

            else:
                print("Not found")
        else:
            break

except EOFError:
    pass
