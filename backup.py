import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

soccer_data = pd.read_csv("mysheet.csv")

soccer_data.head()

# for col in soccer_data.columns:
#     print(col)

# for col in soccer_data.columns:

#     i = 0

#     # print(col)
#     # print(soccer_data['Age'])
#     print(soccer_data["Squad"][i])
#     i = i+1

#     if i ==21:
#         break

count = 0
while (count < 20):   

    print(soccer_data["Squad"][count])
    count = count + 1


# print(soccer_data["Squad"][0:21].keys())
# soccer_data["Squad"].value_counts()

# soccer_data["Squad"].value_counts()
# soccer_data['Age'].value_counts()

# soccer_data["Squad"].value_counts()
# soccer_data["Squad"]
    