def check_subset():
    int(input())
    s1 = list(map(int, input().split()))
    int(input())
    s2 = list(map(int, input().split()))
    for i in s1:
        if i not in s2:
            return False
    return True
        
for i in range(int(input())):
    print(check_subset())
