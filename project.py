#This is a little project with Pandas 
#Here is Pandas 
import pandas as pd

information = {"Name of warrior ":["Mike","Miguel","Elena","Jack","Goku","Pedro"],
"Power":["1200","200","3900","23445","75678","12346"],
"Origin":["Earth","Jupiter","Neptune","Earth","Jupiter","Neptune"]
}

df = pd.DataFrame(information)

print(df)