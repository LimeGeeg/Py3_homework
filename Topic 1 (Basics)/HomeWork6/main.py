import random
import math
import settings as st
count_students = int(input("Введите кол.во студентов: "))

dict = {}
dict_result = {}
result = []
for i in range(count_students):
    name = random.choice(st.NAME_LIST)
    last_name = random.choice(st.LASTNAME_LIST)
    name_and_lastname = f"{name} {last_name}"
    ratings_list = []
    for x in range(10):
        ratings_list.append(random.randint(2, 12))
    dict[name_and_lastname] = ratings_list

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
for value in sorted(dict.values()):
    dict_result[get_key(dict, value)] = (sum(dict[get_key(dict, value)]))/10

count = count_students
for value in sorted(dict_result.values()):
    result.append(f"#{count}: {get_key(dict_result, value)} | Средний бал: {value}\n")
    count -= 1

print(''.join(result))
input()