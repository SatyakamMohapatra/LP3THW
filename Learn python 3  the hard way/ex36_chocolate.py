from sys import exit

def select_waffers(selected,price):
    print("Select Your waffers type")
    print("""
    1 for Chocolate,Price = Rs 25
    2 for BlackCurrent,Price = Rs 30
    """)

    option = int(input("Select any one > "))
    print("\n")
    selected += "Waffers Selected:\t"

    if option == 1:
        selected += "Chocolate waffers"
        price +=55
    elif option == 2:
        selected += "BlackCurrent waffers"
        price +=65
    else:
        print("Not a Valid Option !!")
        stop()
    print(f"{selected} \nTotal: Rs.{price}.00")
    selected +="\n"

    bill(selected,price)

def bill(selected,price):
    print("\n")
    print("---------------------------")
    print(f"{selected} \nTotal: Rs.{price}.00")
    print("---------------------------")
    print("Thanks,Please Visit Again")


def select_chocolate(selected,price):
    print("Select Your chocolate type")
    print("""
    1 for Gems,Price = Rs 55
    2 for Pop,Price = Rs 65
    3 for Chips,Price = Rs 35
    4 for Oreo,Price = Rs 25
    """)
    option = int(input("Select any one > "))
    selected += "chocolate Selected:\t"
    if option == 1:
        selected += "Gems chocolate"
        price +=55
    elif option == 2:
        selected += "Pop chocolate"
        price +=65
    elif option == 3:
        selected += "Chips chocolate"
        price +=35
    elif option == 4:
        selected += "Oreo chocolate"
        price +=25
    else:
        print("Not a Valid Option !!")
        stop()
    print(f"{selected} \nTotal: Rs.{price}.00")
    selected +="\n"

    buy = int(input("1 to Bill,2 to continue to waffers"))
    valid = True
    while valid:
        if buy == 1:
            valid = False
            bill(selected,price)
        elif buy == 2:
            valid = False
            select_waffers(selected,price)
        else:
            print("Select A valid Option")



def select_icecream(selected,price):
    print("Select Your IceCream flavor")
    print("""
    1 for Berry,Price = Rs 50
    2 for Choco,Price = Rs 60
    3 for Vanila,Price = Rs 30
    4 for BlackCurrent,Price = Rs 100
    """)
    option = int(input("Select > "))
    i = 0
    selected = "IceCream Selected:\t"
    while i<2:
        if option == 1:
            selected += "Berry IceCream, "
            price +=50
        elif option == 2:
            selected += "Choco IceCream, "
            price +=60
        elif option == 3:
            selected += "Vanila IceCream, "
            price +=30
        elif option == 4:
            selected += "BlackCurrent IceCream, "
            price +=100
        else:
            print("Not a Valid Option !!")
            stop()
        i +=1
        print(f"{selected} \nTotal: Rs.{price}.00")
        if i< 2:
            option = int(input("Select 2nd flavor > "))

    selected = selected[:len(selected)-1]
    selected +="\n"

    buy = int(input("1 to Bill,2 to continue to chocolate"))
    valid = True
    while valid:
        if buy == 1:
            valid = False
            bill(selected,price)
        elif buy == 2:
            valid = False
            select_chocolate(selected,price)
        else:
            print("Select A valid Option")


def stop():
    print("Please do Visit again! Thank you")
    exit(0)

def start():
    print("Welcome to Ice Cream Factory!!!1")
    print("You can create customized Ice Cream and enjoy!")
    print("Do You like to have some Ice cream?")
    option = input("Yes or No > ")
    selected = ""
    price = 0

    if option.lower() == "Yes".lower():
        #Select IceCream
        select_icecream(selected,price)
    else:
        stop()

start()
