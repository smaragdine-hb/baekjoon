a = int(input())

for i in range(a):
    h,w,n = map(int,input().split())
    if n%h != 0:
        if n//h+1<10:
            print(n%h,0,n//h+1,sep="")
        else:
            print(n%h,n//h+1,sep="")
    else:
        if n//h<10:
            print(h,0,n//h,sep="")
        else:
            print(h,n//h,sep="")