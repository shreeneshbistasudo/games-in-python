operator=input("select a operator(+ - / *)")
num1=float(input("type the 1st num: "))
num2=float(input("type the 2nd num: "))

if operator=='+':
    
    print(num1+num2)
    
elif operator=='-':
    print(num1-num2)
    
elif operator=='/':
    print(num1/num2)
    
elif operator=='*':
    print(num1*num2)
    
else:
    
    print(f"{operator} is not valid")