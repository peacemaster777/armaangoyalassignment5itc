#ques4
rows = 5

for i in range(rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()
     #upper half is printed

for i in range(rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
    #lower half is printed