import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

soccer_data = pd.read_csv("player1.csv")


font = {'size'   :25}
plt.rc('font', **font)

# soccer_data.head()

# count = 0
# while (count < 20):   

#     team = soccer_data["Squad"][count]

#     print(soccer_data["Squad"][count])
#     count = count + 1


print("~~~~~~~~~~~~")
# print(soccer_data["Squad"])
# print("~~~~~~~~~~~~")

for col in soccer_data.columns:
    print(col)



#matplotlib

# font = {'size'   : 50.5}
# plt.rc('font', **font)

fig, ax = plt.subplots()


# hide axes
fig.patch.set_visible(False)
ax.axis('off')
ax.axis('tight')

#create pandas DataFrame
df = pd.DataFrame(np.random.randn(20, 6), columns=['Player', 'xG', 'Gls', "xG-difference","Sh/90","SoT/90"])

xList = list(soccer_data["Player"])
zList = list(soccer_data["xG"])
yList = list(soccer_data["Gls"])
aList = list(soccer_data["Sh/90"])
bList = list(soccer_data["SoT/90"])
# z = list(soccer_data["Ast"])

#create values for table

table_data=[
    [xList[0], zList[0], yList[0], round(zList[0] - yList[0],2), aList[0], bList[0]],
    [xList[1], zList[1], yList[1], round(zList[1] - yList[1],2), aList[1], bList[1]]
    ,
    [xList[2], zList[2], yList[2], round(zList[2] - yList[2],2), aList[2], bList[2]]
    ,
    [xList[3], zList[3], yList[3], round(zList[3] - yList[3],2), aList[3], bList[3]]
    ,
    [xList[4], zList[4], yList[4], round(zList[4] - yList[4],2), aList[4], bList[4]]
    ,
    [xList[5], zList[5], yList[5], round(zList[5] - yList[5],2), aList[5], bList[5]]
    ,
    [xList[0+6], zList[0+6], yList[0+6], round(zList[0+6] - yList[0+6],2), aList[0+6], bList[0+6]],
    [xList[1+6], zList[1+6], yList[1+6], round(zList[1+6] - yList[1+6],2), aList[1+6], bList[1+6]]
    ,
    [xList[2+6], zList[2+6], yList[2+6], round(zList[2+6] - yList[2+6],2), aList[2+6], bList[2+6]]
    ,
    [xList[3+6], zList[3+6], yList[3+6], round(zList[3+6] - yList[3+6],2), aList[3+6], bList[3+6]]
    ,
    [xList[4+6], zList[4+6], yList[4+6], round(zList[4+6] - yList[4+6],2), aList[4+6], bList[4+6]]
    ,
    [xList[5+6], zList[5+6], yList[5+6], round(zList[5+6] - yList[5+6],2), aList[5+6], bList[5+6]]
    ,

    # [xList[0+12], zList[0+12], yList[0+12], round(zList[0+12] - yList[0+12],2), aList[0+12], bList[0+12]],
    # [xList[1+12], zList[1+12], yList[1+12], round(zList[1+12] - yList[1+12],2), aList[1+12], bList[1+12]]
    # ,
    # [xList[2+12], zList[2+12], yList[2+12], round(zList[2+12] - yList[2+12],2), aList[2+12], bList[2+12]]
    # ,
    # [xList[3+12], zList[3+12], yList[3+12], round(zList[3+12] - yList[3+12],2), aList[3+12], bList[3+12]]
    # ,
    # [xList[4+12], zList[4+12], yList[4+12], round(zList[4+12] - yList[4+12],2)]
    # ,
    # [xList[5+12], zList[5+12], yList[5+12], round(zList[5+12] - yList[5+12],2)]


    # ["Player 2", 20],
    # ["Player 3", 33],
    # ["Player 4", 25],
    # ["Player 5", 12]
]

#create table
table = ax.table(cellText=table_data, colLabels=df.columns, loc='center')

table.auto_set_font_size(False)
table.set_fontsize(12)

# table.set_fontsize(30)
table.scale(1.5, 1.5)  # may help

# df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))

# ax.table(cellText=df.values, colLabels=df.columns, loc='center')

fig.tight_layout()


# x = list(soccer_data["Squad"])
# y = list(soccer_data["Gls"])
# z = list(soccer_data["Ast"])



# fig1, (ax1, ax2) = plt.subplots(2,1)

# ax1.bar(x, y)
# ax1.set_ylabel("Goals")
# ax2.bar(x, z, color='red')
# ax2.set_ylabel("Ast")



plt.show()


print("~~~~~~~~~~~~")




# Rk
# Player
# Nation
# Pos
# Squad
# Age
# Born
# 90s
# Gls
# Sh
# SoT
# SoT%
# Sh/90
# SoT/90
# G/Sh
# G/SoT
# Dist
# FK
# PK
# PKatt
# xG
# npxG
# npxG/Sh
# G-xG
# np:G-xG
# Matches