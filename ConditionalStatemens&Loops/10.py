#Write a Python program to calculate the sum and average of n integer numbers (input from the user). Input 0 to finish.
total_sum = 0
count = 0

while True:
    num = int(input("Enter an integer number (enter 0 to finish): "))
    if num == 0:
        break
    total_sum += num
    count += 1

if count != 0:
    average = total_sum / count
else:
    average = 0

print("Sum of the numbers:", total_sum)
print("Average of the numbers:", average)
