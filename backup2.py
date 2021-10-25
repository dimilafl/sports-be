import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

soccer_data = pd.read_csv("mysheet.csv")

soccer_data.head()

count = 0
while (count < 20):   

    team = soccer_data["Squad"][count]

    print(soccer_data["Squad"][count])
    count = count + 1


# print("~~~~~~~~~~~~")
# print(soccer_data["Squad"])
# print("~~~~~~~~~~~~")

for col in soccer_data.columns:
    print(col)



#matplotlib

x = list(soccer_data["Squad"])
y = list(soccer_data["Gls"])
z = list(soccer_data["Ast"])

font = {'size'   : 4.5}
plt.rc('font', **font)

fig1, (ax1, ax2) = plt.subplots(2,1)


# fig1.set_figheight(2.5)
# fig1.set_figwidth(500)

# fig1.rcParams.update({'font.size': 4.5})

ax1.bar(x, y)
# ax1.set_title("Goals per Team")
# ax1.set_xlabel("Teams")
# ax1    ("Goals")
ax1.set_ylabel("Goals")

ax2.bar(x, z, color='red')
# ax2.set_title("Assists per Team")
# ax2.set_xlabel("Teams")
ax2.set_ylabel("Ast")

fig2, (ax3, ax4) = plt.subplots(2,1)



y1 = list(soccer_data["Gls"])
z1 = list(soccer_data["Poss"])

ax3.bar(x, y1)
ax3.set_ylabel("Goals")

ax4.bar(x, z1, color='green')
ax4.set_ylabel("Possession")



# plt.rcParams['font.size'] = '2'

# fig1.rcParams['font.size'] = '4.5'
# plt.figure(figsize=(250,5))
# plt.bar(list(soccer_data["Squad"]),list(soccer_data["Poss"]))
plt.show()


print("~~~~~~~~~~~~")





# ax1.s("Goals")

# ax1.set_figheight(15)
# ax1.set_figwidth(15)
# ax1.figure(figsize=(250,5))


# ax1.figure(figsize=(250,5))


# plt.set_ylabel("Possesion")
# plt.bar(list(soccer_data["Squad"]),list(soccer_data["Gls"]))
# plt.bar(list(soccer_data["Squad"]),list(soccer_data["Ast"]))
# ax1.show()


# Squad
# # Pl
# Age
# Poss
# MP
# Starts
# Min
# 90s
# Gls
# Ast
# G-PK
# PK
# PKatt
# CrdY
# CrdR
# Gls p90
# Ast p90
# G+A p90
# G-PK p90
# G+A-PK  p90
# xG
# npxG
# xA
# npxG+xA
# xG p90
# xA p90
# xG+xA p90
# npxG p90
# npxG+xA p90