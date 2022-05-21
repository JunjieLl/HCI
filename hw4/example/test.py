
import pandas as pd

df = pd.read_csv("./lab3-datasets/black-friday/BlackFriday.csv",encoding = 'ISO-8859-1')

print(df["Product_ID"].unique().shape)