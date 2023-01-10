def user_calculator():
    num1=(input("enter a number: "))
    num2=(input("enter second number: "))
    try:
        a=int(num1)
        b=int(num2)
        sum1=a+b
        return(sum1)
    except ValueError:
        return("you entered a string, enter a number")
print(user_calculator())
   
 
   