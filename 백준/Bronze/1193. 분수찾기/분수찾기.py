a = int(input())
b = 0
c = 0 
while True:
    c += 1 #
    b += c # 총 칸수
    if a == 1:
        print("1/1")
        break
    elif b>=a:
        if c % 2 ==0:
            print(a-(b-c),"/",b-a+1,sep="")
        else:
            print(b-a+1,"/",a-(b-c),sep="")
        break
