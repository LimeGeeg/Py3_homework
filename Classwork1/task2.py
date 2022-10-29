result_map = []

def counter(number):

    if number == 1:
        result_map.append("⠀*")
        result_map.append("\n")

    for i in range(number):
        if i % 2 == 0:
            continue

        if i == 1:
            result_map.append("*")
            result_map.append("\n")

        result_map.append("*"*(i+2))
        result_map.append("\n")

    while number >= 1:
        number -= 1
        if number % 2 == 0:
            continue

        result_map.append("*"*number)
        result_map.append("\n")

    return result_map

while True:
    result_map = []
    number = int(input("Введите целое положительное нечетное число: "))
    if number >= 1 and number % 2 == 0:
        print("Число не соответствует требованиям")
        continue

    rs = counter(number)
    print("----------------")
    print(''.join(rs))
    print("----------------")