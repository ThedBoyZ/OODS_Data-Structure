def word_congrat(word_type):
    keep_subword_after = ''
    reset = 1
    print_outword =[]
    for word_index,word in enumerate(word_type):
        words = word.split(",")
        for sub_word in words:
            sub_word = sub_word.strip()
            if sub_word.startswith("P"):
                sub_word = sub_word[2:].strip()
                if word_index == 0 or reset == 1:
                    keep_subword_before = sub_word[-2:].strip()
                    reset = 0
                else:
                    keep_subword_after = sub_word[:2].strip()                    
                keep_subword_before = keep_subword_before.lower()
                keep_subword_after = keep_subword_after.lower()
                if len(keep_subword_after) == 0:
                    keep_subword_after = keep_subword_before
                    print_outword.append(sub_word)
                    print(f"'{sub_word}' -> ['{sub_word}']")
                elif keep_subword_before == keep_subword_after:
                    keep_subword_after = keep_subword_before
                    print_outword.append(sub_word)
                    print(f"'{sub_word}' -> {print_outword}")
                else:
                    print(f"'{sub_word}' -> game over") 

            elif sub_word.startswith("R"):
                sub_word = sub_word[2:].strip()
                print("game restarted")
                keep_subword_after = ''
                keep_subword_before = ''
                print_outword = []
                reset = 1
            elif sub_word.startswith("X"):
                return  
            else:
                print(f"'{sub_word}' is Invalid Input !!!") 
                return 

print("*** TorKham HanSaa ***")
word_type = input("Enter Input : ").split(",")

word_congrat(word_type)