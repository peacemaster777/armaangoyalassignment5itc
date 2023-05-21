#ques6
def is_prime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print("Prime numbers within the range", start, "to", end, "are:")
for a in range(start, end + 1):
    if is_prime(a):
        print(a)
