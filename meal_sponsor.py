
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")
import random
n= len(names)
a=random.randint(0,n-1)
print(f"{names[a]} is going to buy meal today!")
