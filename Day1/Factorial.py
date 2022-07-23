def factorial(a):
       if a==1:
        return 1
       else:
        return (a* factorial(a-1))
num=int(input("Enter the number:"))
result=factorial(num)
print("Factorial of",num,"is",result)

