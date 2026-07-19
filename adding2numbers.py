def add_two_numbers(x, y):
    return x + y    

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = add_two_numbers(a, b)
print("The sum of", a, "and", b, "is:", c)
 
d= int(input("Enter the third number: "))
e= int(input("Enter the fourth number: "))
f= d - e
print("The difference of", d, "and", e, "is:", f)

h= a+b+f
print("The final result after adding the sum and the difference is:", h)
