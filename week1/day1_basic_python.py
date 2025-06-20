#type() in python
# name="Alice"
# print(type(name))

# age=25
# print(type(age))


#concatination in python
# a=5
# b="man"
# c=a+int(b)
# print (c)

# a=5
# b="man"
# c=str(a)+b
# print (c)

#Conditional/control statement
#elif statement
# number=int(input("Enter a number:")) #this line takes input from user

# if number>0:
#     print("The number is positive")
# elif number<0:
#     print("the number is negative")
# else:
#     print("The number is zero")
    
#loops
#for loops
# for i in range(1,11):
#     print(i)


#slicing in python
# num=[1,2,3,4,5,6,7]
# # check=num[0:6:2]
# check=num[:6:2]
# print(check)


# control statement practice
# age=int(input("Age:"))
# if (age>=18 and age<100):
#     print("You are eligile to vote")
# elif (age<18 and age>0):
#     print("you are not eligible to vote")
# else:
#     print("invalid age")


#assigment-WAP to check weather an entered number is odd or even
num=int(input("Enter number:"))
if num==0:
    print("Division by zero")
elif num%2==0:
    print("the number is even")
elif num%2!=0:
    print("The number is odd")
else:
    print("Invalid number")
