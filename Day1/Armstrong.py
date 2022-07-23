def armstrong():
    num=int(input("Enter the number:"))
    temp=num
    arm=0
    while num>0:
        dig=num%10
        arm= arm+ dig**3
        num=num//10
    if temp==arm:
         print("yes, it is an armstrong number")
    else:
        print("not an armstrong number")
armstrong()