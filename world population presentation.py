import matplotlib.pyplot as plt
import numpy as np
gdp=[1000, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000, 2500, 3000, 3400, 3700, 3900, 4000, 4100, 4500, 4700, 4800, 5000, 5500, 5900, 6000, 6500, 7000]
lifeexpectancy=[20, 23, 24, 30, 50, 34, 10, 37, 60, 67, 78, 77, 80, 60, 30, 22, 55,58, 63, 18, 27, 34, 23, 24, 25, 26]
#col=np.array("red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta","red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta")
colors=np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120,125])
sizes=np.array([5,10,20,30,100,40,20,50,50,70,20,30,60,25,57,90,38,22,15,89,67,55,77,80,40,50])
plt.scatter(gdp,lifeexpectancy,s=sizes,c=colors,alpha=0.8,cmap='viridis')

plt.colorbar()
plt.xscale('log')
plt.xlabel('GDP')
plt.ylabel('life expectancy')
plt.title('World population')
plt.yticks([10,20,30,40,50,60,70,80],['1K','2K','3K','4K','5K','6K','7K','8K'])
plt.text(1300,24,'India')
plt.text(1900,60,'China')
plt.grid(axis='y', linestyle='--',linewidth='0.4')

plt.show()