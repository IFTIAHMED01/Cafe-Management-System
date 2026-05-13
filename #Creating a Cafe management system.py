#Creating a Cafe management system

menu = {
    'Chicken Breast': 40,
    'Chicken Wings': 20,
    'Beef/ Chicken Burger': 60,
    'Brownie': 15,
    'Coffee': 10
}

#Printing the menu
print("Welcome to Barcode Restaurant")

print("Chicken Breast: BDT 40\nChicken Wings: BDT 20\nBeef/Chicken Burger: BDT 60\nBrownie: BDT 15\nCoffee: BDT 10" )

Total_Price = 0

Answer = input("Are you ready for  order? (Yes/No)")

if Answer == "Yes":

 item_1 = input("Enter the name of item you want to order = ")
 if item_1 in menu:
    Total_Price+= menu[item_1]
    print(f"Your item {item_1} has been added to your order")

 else:
    print(f"Ordered item {item_1} is not available yet!")


 anotheritem = input("Do you want to add another item? (Yes/No)")
 if anotheritem == "Yes":
    item_2 = input("Enter the name of item you want to order =")
    if item_2 in menu:
        Total_Price+= menu[item_2]
        print(f"Your item {item_1} has been added to your order")
    
    else:
        print(f"Ordered item {item_1} is not available yet!")

 print(f"The amount of items to pay is BDT {Total_Price}")

print("Thank you for coming to the Restaurant")





