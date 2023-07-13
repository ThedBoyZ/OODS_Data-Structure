print("*** Fun with countdown ***")
number_list = input("Enter List : ").split()
count_list = []
countdown_list = []
count = 0
countdown_list_success = []
for i in range(len(number_list)):
    if i < len(number_list)-1 and int(number_list[i]) == int(number_list[i+1])+1 :
        count_list.append(int(number_list[i]))
    else:
        count_list.append(int(number_list[i]))

        if len(count_list) > 1 and count_list[-1] == 1:
            countdown_list.append(count_list)
            count+=1
        if len(count_list) == 1 and count_list[0] == 1:
            countdown_list.append(count_list)
            count+=1
        count_list = []

countdown_list_success.append(count)
countdown_list_success.append(countdown_list)
print(countdown_list_success)