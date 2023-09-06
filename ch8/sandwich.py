import pyinputplus as pyip
cost = 0
bread = pyip.inputMenu(["wheat", "white", "sourdough"],prompt="What kind of bread would you like?\n")
if bread == "white":
    cost = cost + 1
else:
    cost = cost + 2
protein = pyip.inputMenu(["chicken", "turkey", "ham", "tofu"], prompt="What kind of protein?\n")
if protein == "chicken" or protein == "turkey":
    cost = cost + 1
elif protein == "ham":
    cost = cost + 2
else:
    cost = cost + 3
cheeseYesNo = pyip.inputYesNo("Would you like cheese with that?\n")
if cheeseYesNo == "yes":
    cheese = pyip.inputMenu(["cheddar", "Swiss", "mozzarella"], prompt="What kind?\n")
    if cheese == "mozzarella":
        cost = cost + 1
    else:
        cost = cost + 2
dressing = pyip.inputYesNo("Would you like that dressed?\n")
if dressing == "yes":
    cost = cost + 2
sandwiches = pyip.inputInt("How many would you like?\n", min=1)
cost = cost * sandwiches
print("That will be $%s" % cost)