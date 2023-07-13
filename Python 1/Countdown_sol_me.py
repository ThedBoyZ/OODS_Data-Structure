print("*** Fun with countdown ***")
number_list = input("Enter List : ").split()
count_list = []
countdown_list = []
count = 0
for i in range(len(number_list)):
    check = 1
    print(number_list[i])
    if i < len(number_list)-1 and int(number_list[i]) == int(number_list[i+1])+1 :
        # if len(count_list) == 0:
        #     count_list.append(int(number_list[i]))
        count_list.append(int(number_list[i]))
    # elif i+1 == len(number_list)-1 and int(number_list[i+1]) == 1:
    #     count_list.append(int(number_list[i+1])) 
    else: 
        check = 0
    if len(count_list) > 0 and check == 0:
        countdown_list.append(count_list)
        count_list = []
    count+=1   
print(countdown_list)       