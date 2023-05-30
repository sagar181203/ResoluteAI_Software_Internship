# Trying with the Git Hub
# factorial of a number

def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    
num=int(input("Enter the Number: "))
print("The factorial of ",num,"is : ",factorial(num))
# we doing this for modified