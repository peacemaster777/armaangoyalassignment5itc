#ques7
a = 1
b = 500

print("Numbers which are multiples of 7 and divisible by 11 in the range 1 to 500:")
for i in range(a, b + 1):
    if i % 7 == 0 and i % 11 == 0:
        print(i)
