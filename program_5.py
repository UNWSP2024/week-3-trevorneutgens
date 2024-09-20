# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost.

# variables that will hold the final prined values
subtotal = 0.00
tax = 0.00
total_cost = 0.00

# if statement to get the users dog choice
dog_choice = input("Choose Hot Dog or Chili Dog:")
if dog_choice == 'Hot Dog':
    subtotal = 3.50
    print("+$3.50")
elif dog_choice == 'Chili Dog':
    subtotal = 4.50
    print("+$4.50")
else:
    print("Sorry, your answer is invalid. Please select 'Hot Dog' or 'Chili Dog'.")

# if statement to see if user wants cheese
cheese_choice = input("Want Cheese? Please type 'Yes' or 'No':")
if cheese_choice == 'Yes':
    subtotal = subtotal + 0.50
    print("+$0.50")
elif cheese_choice == 'No':
    print("+$0.00")
else:
    print("Sorry, your answer is invalid. Please select 'Yes' or 'No'.")

# if statement to see if user wants peppers
peppers_choice = input("Want Peppers? Please type 'Yes' or 'No':")
if peppers_choice == 'Yes':
    subtotal = subtotal + 0.75
    print("+$0.75")
elif peppers_choice == 'No':
    print("+$0.00")
else:
    print("Sorry, your answer is invalid. Please select 'Yes' or 'No'.")

# if statement to see if user wants onions
onions_choice = input("Want Grilled Onions? Please type 'Yes' or 'No':")
if onions_choice == 'Yes':
    subtotal = subtotal + 1.00
    print("+$1.00")
elif onions_choice == 'No':
    print("+$0.00")
else:
    print("Sorry, your answer is invalid. Please select 'Yes' or 'No'.")
tax = subtotal * 0.07
total_cost = subtotal + tax
print(f'Subtotal: $ {subtotal:.2f}')
print(f'Tax: $ {tax:.2f}')
print(f'Total Cost: $ {total_cost:.2f}')