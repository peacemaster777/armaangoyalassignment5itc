#ques5
def print_alphabet_triangle(rows):
    current_alphabet = ord('A')  # Start with 'A'
    count = 1

    for i in range(rows):
        for j in range(count):
            print(chr(current_alphabet), end='')
            current_alphabet += 1

            if current_alphabet > ord('Z'):
                current_alphabet = ord('A')

        print()
        count += 1

#usage
num_rows = int(input("Enter the number of rows: "))
print_alphabet_triangle(num_rows)
