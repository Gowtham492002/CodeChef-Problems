t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split())
    if w+y*z>x:
        print("overflow")
    elif w+y*z<x:
        print("unfilled")
    else:
        print("filled")