def get_data(data):
    gender = []
    weight = []
    height = []
    # WRITE YOUR CODE HERE
    data_list = data.read().split('\n')
    g,h,w = data_list.pop(0).split(',')

    for item in data_list:
        gen,heig,weig = item.split(',')
        gender.append(1) if gen == '"Male"' else gender.append(0)
        weight.append(float(weig)/ 2.205)
        height.append(float(heig)*2.54)
        
    return gender,weight,height