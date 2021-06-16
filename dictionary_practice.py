food_price = {"Chicken": 1.59, "Beef": 1.99, "Cheese": 1.00, "Milk": 2.50}

phone_nums = {"Emergency": 911, "Mom": 4153369995, "Dad": 5109996666, "School": 8115553333}

chicken_cost = food_price["Chicken"]
beef_cost = food_price["Beef"]
cheese_cost = food_price["Cheese"]
milk_cost = food_price["Milk"]

print(f"chicken costs {chicken_cost}")
print(f"beef costs {beef_cost}")
print(f"cheese costs {cheese_cost}")
print(f"milk costs {milk_cost}")

#lab 3- step VI

shoe_inventory = {"Jordan 13": 1, "Yeezy": 8, "Foamposite":10, "Airmax": 5, "SB Dunk": 20}

#lab 3- step VII

shoe_inventory["SB Dunk"]-=2
shoe_inventory["Yeezy"]+=1

for x in shoe_inventory:
    shoe_inventory[x]+=7

for x in shoe_inventory:
    shoe_inventory[x]-=3 
    print(shoe_inventory[x])

#lab 3- step VIII

food_price["Lemon"] = 0.85
food_price["Lettuce"] = 3.99
food_price["Pork"] = 2.99

phone_nums["Aunt"] = 5101234567
phone_nums["Bestie"] = 4158881111
phone_nums["Cousin"] = 5105551212

shoe_inventory["Jordan 4"] = 6
shoe_inventory["Jordan 1 High Top"] = 4
shoe_inventory["Converse"] = 13

#lab 3- step IX

del food_price["Chicken"]
del food_price["Beef"]
print(food_price)

del phone_nums["Dad"]
del phone_nums["School"]
print(phone_nums)

del shoe_inventory["Jordan 13"]
del shoe_inventory["Foamposite"]
print(shoe_inventory)

#lab 3- step X