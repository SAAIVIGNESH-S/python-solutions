for i in range(int(input())):
    num = input()
    if len(num) != 10:
        print("NO")
    else:
        if num.isdigit():
            if num[0] >= '7' and num[0] <= '9':
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
