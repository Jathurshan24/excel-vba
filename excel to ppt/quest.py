inputList = [2,1,3,4,1,1,6,4,8]

def triplets_average(input):
    avg_list = []
    for i in  range(1,len(input)+1):
        if(i%3 == 0):
            avg =  (input[i-3] + input[i-2] + input[i-1])/3
            avg_list.append(int(avg))
    print(avg_list)

triplets_average(inputList)