def plate_broke(frequency):
    no_freq = ""
    weight_plate = ""
    memory_plate = 0
    memory_freq = 0
    stack_weight = []
    stack_frequency = []
    stack_break = []

    for index, plate in enumerate(frequency):
        for sub_index, sub_word in enumerate(plate):
            if sub_word == " ":  
                no_freq = plate[sub_index + 1:]
                weight_plate = plate[:sub_index]
                stack_weight.append(weight_plate) 
                stack_frequency.append(no_freq)
                if index == 0:
                    memory_plate = weight_plate = plate[:sub_index]
                if int(memory_plate) < int(weight_plate):
                    count = len(stack_weight)
                    for i in range(count, 0, -1):
                        if int(weight_plate) > int(stack_weight[i-1]):
                            stack_weight.pop(i-1)
                            stack_break.append(stack_frequency[i-1])
                            stack_frequency.pop(i-1)       
                memory_plate = weight_plate
    
    print(*stack_break, sep="\n")

sonic = input("Enter Input : ").split(",")
plate_broke(sonic)