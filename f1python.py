# # # message = "  hello's , world "
# # # # print(message.strip()) #remove leading and trailing spaces
# # # # print(message.lower()) #convert to lowercase
# # # # print(message.split(',')) #split by comma
# # # print(message.replace("hello's","feature")) #replace 'bug' with 'feature'

# # # num = 10
# # # num2 = 0.34

# # # print(type(num2))
# # # print(type(num))
# # # # print(type(message)) #check type of variable 
# # num = 0
# # num1 = 10
# # # # print(num + num1) #addition
# # # print(num + num1) #addition


# # # # print(num - num1) #subtraction
# # # print(num1 - num) #subtraction


# # # # print(num * num1) #multiplication
# # # print(num * num1) #multiplication


# # # # print(num / num1) #division
# # # print(num1 / num) #division


# # # # print(num // num1) #floor division
# # # print(num1 // num) #floor division print the quotient without the decimal part


# # # # print(num % num1) #modulus
# # # print(num1 % num) #modulus print the remainder of the division the number after the decimal point


# # # # print(num ** num1) #exponentiation /to the power of
# # # print(num1 ** num) #exponentiation print the result of raising the first number to the power of the second number

# # # # print(num1 == num) #equal to
# # # print(num1 == num) #equal to


# # # # print(num1 != num) #not equal to 
# # # print(num1 != num) #not equal to


# # # print(num1 > num) #greater than
# # if num > 0:
# #     print("num is greater than 0") # print(num1 > num) #greater than
# # elif num == 0:
# #     print("num is equal to 0")
# # else:
# #     print("num is a negative number") # print(num1 > num) #greater than

# # num = int(input("Enter a number: "))
# # num1 = int(input("Enter another number: "))

# # if num > num1:
# #     print(num, "is greater than", num1)
# # elif num1 > num:
# #     print(num, "is less than", num1)
# # else:
# #     print(num, "is equal to", num1)

# # #example of a for loop in python
# # fruits = ["appple", "banana", "mango"]
# # # print(fruits[0])

# # for fruit in fruits:
# #     print(fruit)

# # #example of a while loop in python
# # count = 4

# # while count <= 20:
# #     print(count)
# #     count += 1  # increment the count by 1

# #example of loops Control Statements in Python


# fruits = ["apple", "banana", "mango", "orange", "grape"]
# for fruit in fruits:
#     if fruit == "mango":
#         break
#     print(fruit)
    
#     print()
    
# for fruit in fruits:
#     if fruit == "mango":
#         continue #skip the rest of the loop for this iteration
#     print(fruit)
    
#     print()
# for fruit in fruits:
#     if fruit == "mango":
#         pass  # do nothing, just a placeholder
#     print(fruit)

verenga = 0

while verenga < 10:
    print(verenga)
    verenga += 1  # increment the counter by 1
    if verenga == 5:
        continue # exit the loop when verenga is 5