#step 1
US_cities= ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]

print(US_cities)

#step 2
rainbow_colors= ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink", "White", "Grey", "Black"]

print(rainbow_colors)

#step 3
print(US_cities[2], US_cities[-3], US_cities[0])

print(rainbow_colors[7], rainbow_colors[5], rainbow_colors[6])

#step 4
US_cities[0]= "San Francisco"
print(US_cities[0])

US_cities[2]="Brooklyn"
print(US_cities[2])

US_cities[-3]="Hollywood"
print(US_cities[-3])

US_cities[-5]="Tampa"
print(US_cities[-5])

#step 5
US_cities.append("New Jersey")
US_cities.extend(["Santa Cruz", "Selma" ])
US_cities.insert(7, "Washington D.C.")

print(US_cities)

#step 6
US_cities.append("Oakland")
US_cities.extend(["New York City", "Los Angeles"])
US_cities.insert(0, "Miami")

print(US_cities)

#step 7
del US_cities(2)
US_cities.pop(5)
US_cities.remove("Oakland")

print(US_cities)

#step 8
#git commit