import os
rs = []

with open("tables.txt", "r") as file:
    for line in file:
        rs.append(line)

fizz = int(rs[0])
buzz = int(rs[1])
count = int(rs[2])

n=0
all_num = []

os.remove('results.txt')
t = open('results.txt', 'w')

for i in range(count):
     if n == count:
         print(all_num)
     else:
         n += 1
         if n % buzz == 0 and n % fizz == 0:
             all_num.append("FB")
         elif n % buzz == 0:
             all_num.append("B")
         elif n % fizz == 0:
             all_num.append("F")
         else:
             all_num.append(str(n))

with open("results.txt", "a") as file:
    file.write(' '.join(all_num))

print(f"Result: {' '.join(all_num)}")

input()