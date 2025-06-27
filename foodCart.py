#create a shopping cart program that will continuously ask the user for a food product and the price of the product.
#Have an exit option if the user wishes to stop adding products to their cart.
#At the end, display the total cost of all products in the cart.

foods = []
prices = []
total = 0.0

while True:
    food = input("Enter a food product or type Q to quit: ")
    if food.lower() == 'q':
        break
    
    else:
        price = float(input(f"Enter the price of {food}: R"))
        foods.append(food)
        prices.append(price)
        
print("-----------Your cart--------")
        
for food in foods:
    print(food, end= " ")
            
        # # print("------------Your Total Price----------------")
for price in prices:
    total += price
    print("\n") #skip line for better readability          
    print(f"Total cost: R{total}")


# while True:
#     food = input("Enter a food product or type Q to quit: ")
#     if food.lower() == 'q':
#         print("\n-----------Your cart--------")
#         for i in range(len(foods)):
#             print(f"{foods[i]} - R{prices[i]}")
        
#         print(f"\nTotal cost: R{total_cost}")
#         break
#     else:
#         price = float(input(f"Enter the price of {food}: R"))
#         foods.append(food)
#         prices.append(price)
#         total_cost += price  # ✅ Only add current price
