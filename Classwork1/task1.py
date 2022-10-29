def counter(nm_appartment, ct_appartment, ct_floors):
    floor = nm_appartment / ct_appartment
    num = floor - ct_floors
    entrance = 1

    while num > 0:
        entrance += 1

    final_floor = round(floor)
    final_entrance = round(entrance)

    return final_floor, final_entrance, ct_floors

number_of_appartament = int(input("Введите номер квартиры: "))
count_of_appartament = int(input("Введите кол.во квартир на этаж: "))
count_of_floors = int(input("Введите кол.во этажей на дом: "))

final_floor, final_entrance, count_of_floors = counter(number_of_appartament, count_of_appartament, count_of_floors)

print(f"Этаж заказчика: {final_floor} \n Подъезд: {final_entrance} \n Номер квартиры: №{number_of_appartament}")
input()