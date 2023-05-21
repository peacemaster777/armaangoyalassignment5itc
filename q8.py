#ques8
#  empty lists
numbers = []
positive_numbers = []
negative_numbers = []
odd_numbers = []
even_numbers = []

# Input 10 integers from the user
for i in range(10):
    num = int(input("Enter an integer: "))
    numbers.append(num)

    
    if num > 0:
        positive_numbers.append(num)
    elif num < 0:
        negative_numbers.append(num)
    
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)


number_counts = {}
for num in numbers:
    if num in number_counts:
        number_counts[num] += 1
    else:
        number_counts[num] = 1

# results
print("Positive numbers:", positive_numbers)
print("Negative numbers:", negative_numbers)
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
print("Number of times each number occurs:")
for num, count in number_counts.items():
    print(num, "occurs", count, "time(s)")
