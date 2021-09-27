MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 500,
    "milk": 400,
    "coffee": 200,
}

money = 0

def moneyCheck(y): 
  if y=="input":
    penny = round(0.01 *float(input("\n How many Penny ?")) ,2)
    nickel = round(0.05*float(input("\n How many Nickels ?")),2)
    dime = round(0.10 * float(input("\n How many Dimes ?")),2)
    quarter=round(0.25*float(input("\n How many Quarters ?")),2)
    global totalmoney
    totalmoney =round(penny+nickel+dime+quarter , 2)
    #print(f"{penny}+{nickel}+{dime}+{quarter}={totalmoney}")
  if y == "value":
    
    if totalmoney>= MENU[user_input]["cost"]:
      global money
      money += MENU[user_input]["cost"]
      return True
    else: 
      return False
def resourceCount(): 
  resources["water"]= resources["water"]-MENU[user_input]["ingredients"]["water"]
  resources["milk"] = resources["milk"]-MENU[user_input]["ingredients"]["milk"]
  resources["coffee"]=resources["coffee"]-MENU[user_input]["ingredients"]["coffee"]
  for i in resources: 
    if resources[i]<1:
      print(f"Sorry Not enough {i} , Money Refunded")
      coffee()
      
#def resourceCheck():
#  for i in MENU[user_input]['ingredients']
def coffee():
  machine = True
  while machine: 
    global user_input
    user_input = input("What do u want to take ?(latte/espresso/cappuccino)")
    if user_input == "off": 
      machine=False
    if user_input== "report": 
      print(f'''
    remaining water = {resources ['water']} 
    remaining milk = {resources ['milk']}
    remaining coffee = {resources ['coffee']}
    \nTotal Money Currently : {money}
    ''')
    elif (user_input=="latte" or user_input== "espresso" or user_input== "cappuccino"):  
      print(f"Money required : ${MENU[user_input]['cost']} ")
    
      moneyCheck('input')
      resourceCount()
      if moneyCheck('value') ==  True:
        print(totalmoney)
        print(f"Here is your ☕ {user_input} Enjoy")
        print(f"Here your change {round(totalmoney-MENU[user_input]['cost'],2)}")
      
        
      else: 
        print(f"Not Enough Money")
coffee()