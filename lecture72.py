#Adapt collection part 1
menu_list = []
def show_bill():
    print("---My food---")
    total_price = 0
    for number in range(len(menu_list)):
        print(menu_list)
        total_price = total_price + menu_list[number][1]
    print("Total price: ", total_price)

while True:
    menu_name = input("Please enter menu: ")
    if menu_name.lower() == "exit":
        break
    else:
        menu_price = float(input("Price: "))
        menu_list.append((menu_name,menu_price))

show_bill()