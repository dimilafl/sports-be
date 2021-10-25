import pandas as pd
import numpy as np
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

ax1.bar(x, y)
ax1.set_ylabel("Goals")
ax2.bar(x, z, color='red')
ax2.set_ylabel("Ast")

#figure 2

fig2, (ax3, ax4) = plt.subplots(2,1)

y1 = list(soccer_data["Gls"])
z1 = list(soccer_data["Poss"])

ax3.bar(x, y1)
ax3.set_ylabel("Goals")
ax4.bar(x, z1, color='green')
ax4.set_ylabel("Possession")

#figure 3

# fig3, (ax5) = plt.subplots(2)
fig3, (ax5, ax6) = plt.subplots(2)

y2 = list(soccer_data["xG"])
z2 = list(soccer_data["xA"])

ax5.plot(x, y, color='purple')
ax5.plot(x, y2, color='orange')
ax5.set_ylabel("xG and Gls")

ax6.plot(x, z, color='purple')
ax6.plot(x, z2, color='orange')
ax6.set_ylabel("xA and Ast")
# ax6.plot(x, z2, color='purple')
# ax6.set_ylabel("xA")

#figure 4

# fig3, (ax5) = plt.subplots(2)
fig4, (ax7, ax8) = plt.subplots(2)


ax7.set_axis_off()
#goals regression

ax8.set_title("Linear Regression for Team Goal Output per Game")

games = np.array([1, 3, 5, 7, 1+8, 3+8, 5+8, 7+8, 1+16, 3+16, 5+16, 7+16, 1+24, 3+24, 5+24, 7+24, 1+32, 3+32, 5+32, 7+32])

# y5 = np.array([ 6, 3, 9, 5 ])
plt.plot(games, y, 'o')

m, b = np.polyfit(games, y, 1)


plt.plot(games, m*games + b)



plt.show()


print("~~~~~~~~~~~~")




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