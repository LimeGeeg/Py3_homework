#fizzbuzz code
fizz = int(input("Enter the first number: "))
buzz = int(input("Enter the second number: "))
count = int(input("Enter the number of repetitions: "))

n=0
all_num = []

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
             all_num append(n)

print(f"Result: {all_num}")

input()
