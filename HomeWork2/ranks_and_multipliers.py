import math

num = int(input("Enter a number: "))
save_global_num = num
old_num = num

count = 1
num = num // 10

while num > 0:
     num = num // 10
     count += 1

multipliers = []

for i in range(2, int(math.sqrt(old_num)) + 1):
     while (old_num % i == 0):
         multipliers.append(i)
         old_num = old_num // i

print(f"Digits in {save_global_num}: {count}")
print(f"Multipliers of the number {save_global_num}: {multipliers}")
input()
