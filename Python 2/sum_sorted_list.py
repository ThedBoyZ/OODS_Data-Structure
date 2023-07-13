def sumation_sequence(number_list):
    number_list = [int(i) for i in number_list]
    number_sumation_select = []
    number_sumation_success = []
    if len(number_list) < 3:
        warning = "Array Input Length Must More Than 2"
        return warning
    else: 
        for i in range(len(number_list)):
            for j in range(i + 1, len(number_list)):
                for k in range(j + 1, len(number_list)):
                    if number_list[k] + number_list[j] + number_list[i] == 5:
                        number_sumation_select = sorted([number_list[k], number_list[j], number_list[i]])
                        if number_sumation_select not in number_sumation_success:
                            number_sumation_success.append(number_sumation_select)
        return number_sumation_success

number_list = input("Enter Your List : ").split()

print(sumation_sequence(number_list))