#This is a little project with Pandas 
#Here is Pandas 
import pandas as pd

name = []
power = []
origin = []

num_warrirors = int(input("How many warriors are there? "))

for i in range(num_warrirors):
    name_warrior = input("Insert name of warrior : " )
    name.append(name_warrior)

    power_warrior = input("Insert power of warrior : " )
    power.append(power_warrior)

    origin_warrior = input("Insert origin of warrior  : ")
    origin.append(origin_warrior)
    i+1

    
information = {"Name of warrior ":name,
"Power":power,
"Origin":origin
}
df = pd.DataFrame(information)
print(df)