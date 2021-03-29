import matplotlib.pyplot as plt

languages = ['Python','JavaScript','Java','C','C++','C#','PHP','SQL']
average_salary = ['$119,000','$117,000','$104,000','$103,000','$102,000','$97,000','$94,000','$92,000']
chart1 = [119,117,104,103,102,97,94,92]
x1 = [10,20,30,40,50,60,70,80]

plt.bar(x1,chart1,width=4)
for i,value in enumerate(average_salary):
  plt.text(x1[i]-3,chart1[i]+1,value,size=12)
plt.xticks(x1,languages,size=12)
plt.title('Rank by Average Salary',size=30,pad=15)
plt.show()