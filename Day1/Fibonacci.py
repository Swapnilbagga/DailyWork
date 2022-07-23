def Fibonacci():
     terms=int(input("Enetr the terms:"))
     n1,n2=0,1
     count=0
     if terms<0:
        print("enter a positive number.")
     elif terms==1:
        return n1
     else:
        print("The Fibonaaciseries is:")
        while count<terms:
            print(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            count+=1
        return nth 
Fibonacci()