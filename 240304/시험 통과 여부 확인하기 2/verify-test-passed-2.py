n = int(input())
pass_ = 0

for i in range(n) :
    arr = list(map(int, input().split()))
    sum_val = sum(arr)
    avg = sum_val / 4

    if avg >= 60 :
        print("pass")
        pass_ += 1
    else :
        print("fail")

print(pass_)