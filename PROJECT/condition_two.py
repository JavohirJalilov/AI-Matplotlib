from condition_one import get_data

import matplotlib.pyplot as plt

data = open('weight-height.csv')

def plot_data(gender:list,weight:list,height:list):
    w_male = []
    w_female = []
    h_male = []
    h_female = []
    #WRITE YOUR CODE HERE
    for i in range(len(gender)):
        if gender[i] == 1:
            w_male.append(weight[i])
            h_male.append(height[i])
        else:
            w_female.append(weight[i])
            h_female.append(height[i])
    plt.scatter(w_male,h_male,c='k',label='Male',alpha=0.6)
    plt.scatter(w_female,h_female,c='r',label='Female',alpha=0.6)
    plt.legend(loc='upper left',ncol=2,bbox_to_anchor=(0,1.125))

    plt.show()

gender,weight,height = get_data(data)
plot_data(gender,weight,height)