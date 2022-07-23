a= int(input("enter no."))
b = int(input("enter the divisor:"))
try:
    print(a//b)
except:
    print("error aa gya oye.")
else:
    print("good u can go to google company.")
finally:
    print("good....job done!")
if b==0:
    raise ZeroDivisionError