t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if (y > x):
        print("NO")
    else:
        print("YES")