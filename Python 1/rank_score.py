print(" *** Rank score ***")
input_id = input("Enter ID and Score end with ID : ")
user_list = input_id.split()
student_id = user_list.pop(-1)
print(user_list)
print(student_id)
dict_id_score = {}
for i in range(len(user_list)):
    if (i%2) == 1:
        dict_id_score = {**dict_id_score, user_list[i-1] : float(user_list[i])}
print(dict_id_score)
dict_id_score = sorted(dict_id_score.items(), key=lambda x:x[1], reverse=True)
for i in range(len(user_list)):
    if student_id == user_list[i]:
        print(int((i/2)+1))
        break