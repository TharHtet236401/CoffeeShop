shopStatus = True
userChoice = "";

resource = {
    "Water": 1000,
    "Milk": 500,
    "Coffee": 760,
}

coinValue= {
    "quarters":0.25,
    "dimes":0.1,
    "nickles":0.05,
    "pennies":0.01 
}

resoureRequired= {
    "espresso": {
        "Water": 50,
        "Coffee": 18,
        "Price":6,
        "Milk":0
    },
    "latte": {
        "Water": 200,
        "Milk": 150,
        "Coffee": 24,
        "Price":4
    },
    "cappuccino": {
        "Water": 250,
        "Milk": 100,
        "Coffee": 24,
        "Price":4
    }
}

def resourceCheck(userChoice):
    print (resoureRequired[userChoice])
    waterRequired = resoureRequired[userChoice]["Water"]
    milkRequired = resoureRequired[userChoice]["Milk"]
    coffeeRequired = resoureRequired[userChoice]["Coffee"]
    
    if resource["Water"] < waterRequired:
        print("Sorry there is not enough water")
    elif resource["Coffee"] < coffeeRequired:
        print("Sorry there is not enough coffee")
    elif resource["Milk"] < milkRequired:
        print("Sorry there is not enough milk")
    else:
        finance(userChoice)
        resourceManager(userChoice)


def finance(userChoice):
    price = resoureRequired[userChoice]["Price"];
    print ("It will cost $" + str(price))
    print ("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    
    totalCost = calculator(quarters,dimes,nickles,pennies)
    if totalCost < price:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = totalCost - price
        print("Here is $" + str(change) + " in change.")

def calculator(quarters,dimes,nickles,pennies):
    total = quarters * coinValue["quarters"] + dimes * coinValue["dimes"] + nickles * coinValue["nickles"] + pennies * coinValue["pennies"]
    return total

def resourceManager(userChoice):
    resource["Water"] -= resoureRequired[userChoice]["Water"]
    resource["Coffee"] -= resoureRequired[userChoice]["Coffee"]
    resource["Milk"] -= resoureRequired[userChoice]["Milk"]

while(shopStatus):
    try:
        userChoice = input("What would you like? (espresso/latte/cappuccino):")
        if userChoice == "off":
            shopStatus = False
            print("Thank You")
        elif userChoice == "report":
            print(resource)
        elif userChoice in resoureRequired:
            resourceCheck(userChoice)
        else:
            print("Invalid choice. Please select from espresso, latte, or cappuccino.")
    except KeyError as e:
        print(f"Error: {e}. Please try again.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}. Please try again.")

        
        

    