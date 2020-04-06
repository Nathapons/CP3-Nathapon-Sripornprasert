correct_username = "admin"
correct_password = "123"
username = input("Please input username: ")
password = input("Please input your password: ")

if correct_username == username and correct_password == password:
    print("ID Done")
    print("---Drinking list---")
    print("1.Rock Mountain Soda")
    print("2.Leo")
    drinking_no = int(input(">>"))
    #Check whether client will buy soda or Leo:
    if drinking_no == 1:
        soda_buy_unit = int(input("What number of soda do you buy? "))
        check_soda_return = input("You will return soda to shop?. Input Yes or No: ")
        if check_soda_return == "Yes":
            soda_price = 9
        elif check_soda_return == "No":
            soda_price = 10
        print("soda price: ", soda_buy_unit * soda_price, "Baht")

    elif drinking_no == 2:
        leo_buy_unit = int(input("What number of leo do you buy? "))
        check_buy_can_or_bottle = int(input("You need to buy 1.Can or 2.Bottle: "))
        if check_buy_can_or_bottle == 1:
            leo_price = 35
        elif check_buy_can_or_bottle == 2:
            leo_price = 65
        print("Leo price: ", leo_buy_unit * leo_price, "Baht")
    else:
        print("No number in list")
else:
    print("Error")

