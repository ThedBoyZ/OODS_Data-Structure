def stack_sequence(string_words):
    stack = []
    check = 0
    for word in string_words:
        words = word.split(",")
        for sub_word in words:
            sub_word = sub_word.strip()

            if sub_word.startswith("A"):
                value = sub_word[2:].strip()

                if value != "":
                    stack.append(value)
                    print(f"Add = {value} and Size = {len(stack)}")
                check = 1

            elif sub_word.startswith("P"):
                if len(stack) > 0:
                    popped_value = stack.pop()
                    print(f"Pop = {popped_value} and Index = {len(stack)}")
                elif len(stack) == 0:
                    print("-1")

    if len(stack) <= 0 and check == 1:
        print("Value in Stack = Empty")
    elif len(stack) > 0 and check == 1:
        print("Value in Stack =", *stack, sep=" ")

stack_type = input("Enter Input : ").split(",")
stack_sequence(stack_type)