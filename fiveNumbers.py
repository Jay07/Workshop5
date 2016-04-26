numbers = []

for i in range(1, 6):
    userNumber = int(input("Number: "))
    numbers.append(userNumber)
    i += 1

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is {}".format(sum(numbers)/5))