import matplotlib.pyplot as plt
plt.figure(figsize=(7,7))

percent = [20,1,79]
color = ['#d193ed','#ecf086','#7dafff']
plt.pie(percent,colors=color,autopct='%.1f%%')
plt.legend(['Oxygen','Other gases','Nitrogen'],loc='upper right')
plt.show()