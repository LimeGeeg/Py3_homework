sum = 0
sum_list = []
while True:
     ask = int(input("Enter amount: "))
     sum += ask
     sum_list.append(sum)
     if sum >= 100:
         break
print(sum)
print(sum_list)
