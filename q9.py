#ques9
wordlist = input("Enter a list of words (space-separated): ").split()

wordcounts = {}
for word in wordlist:
    if word in wordcounts:
        wordcounts[word] += 1
    else:
        wordcounts[word] = 1

print("Number of occurrences of each word:")
for word, count in wordcounts.items():
    print(word, ":", count)
