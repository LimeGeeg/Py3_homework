num = int(input("Enter a number: "))

list_of_dividers = []

for i in range(1, num):
     if num % i == 0:
         list_of_dividers.append(i)

list_of_dividers.append(num)
print(f"Result: {list_of_dividers}")

input()
