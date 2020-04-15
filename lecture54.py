def login():
    username = input("Please input username: ")
    password = input("Please input password: ")
    if username == "admin" and password == "1234":
        return True
    else:
        return False
def showMenu():
    print("Done!")
    print("----ishop-----")
    print("1. Vat Calculator")
    print("2. Price Caculator")
    return menuSelect()
def menuSelect():
    userselected = int(input(">>"))
    return userselected
def vatcalculator(TotalPrice):
    result = TotalPrice + (TotalPrice * 7 / 100)
    return result
def priceCalculate():
    return vatcalculator(int(input("1st product price: ")) + int(input("2nd product price: ")))


if login() == True:
    menu_no = showMenu()
    if menu_no == 1:
        print("Your price is ", vatcalculator(float(input("Please input your price: "))))
    elif menu_no == 2:
        print("Your price is ", priceCalculate())
else:
    print("Error!")