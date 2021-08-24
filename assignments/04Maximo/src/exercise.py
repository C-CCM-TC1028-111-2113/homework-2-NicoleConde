numbers = []

for i in range(3):
  num = float(input("Enter the number #{}: ".format(i + 1)))
  numbers.append(num)


higher = numbers[0]

for num in numbers:
    if num > higher:
        higher = num

print("Higher: ", higher)
