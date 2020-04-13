#Adapt collection part 1
menu_list = []
price_list = []
def show_bill():
    print("---My food---")
    for i in range(len(menu_list)):
        print(menu_list[i],menu_price[i])
    print("Total price: ", sum(menu_price))

while True:
    menu_name = input("Please enter menu: ")
    if menu_name.lower() == "exit":
        break
    else:
        menu_price = float(input("Price: "))
        menu_list.append(menu_name)
        price_list.append(menu_price)


def show_bill():
    print("---My food---")
    for i in range(len(menu_list)):
        print(menu_list[i],price_list[i])
    print("Total Price: ", sum(price_list))

show_bill()