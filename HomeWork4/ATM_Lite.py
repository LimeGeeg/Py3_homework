def main(bid):

    count_500 = 0
    while bid >= 500:
        bid -= 500
        count_500 += 1

    count_200 = 0
    while bid >= 200:
        bid -= 200
        count_200 += 1

    count_100 = 0
    while bid >= 100:
        bid -= 100
        count_100 += 1

    count_50 = 0
    while bid >= 50:
        bid -= 50
        count_50 += 1

    count_20 = 0
    while bid >= 20:
        bid -= 20
        count_20 += 1

    count_10 = 0
    while bid >= 10:
        bid -= 10
        count_10 += 1

    count_5 = 0
    while bid >= 5:
        bid -= 5
        count_5 += 1

    count_2 = 0
    while bid >= 2:
        bid -= 2
        count_2 += 1

    count_1 = 0
    while bid >= 1:
        bid -= 1
        count_1 += 1

    print(f"Вы получили сумму {bid} с помощью этих купюр: \n\n 500: {count_500} \n 200: {count_200} \n 100: {count_100} \n 50: {count_50} \n 20: {count_20} \n 10: {count_10} \n 5: {count_5} \n 2: {count_2} \n 1: {count_1}")
    print('-----------------------------------------')
    bid = int(input("Введите сумму получения: "))
    main(bid)

bid = int(input("Введите сумму получения: "))
main(bid)