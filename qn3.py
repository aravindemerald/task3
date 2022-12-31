import string

with open('about.txt', 'r') as f:
    contents = f.read()

words = contents.split()

wordFrequency = {} 
print("The words with 6 letters or more are ")

for word in words:
    word = word.strip(string.punctuation)

    if len(word) >= 6:
        print(word)
        if word in wordFrequency:
            wordFrequency[word] += 1
        else:
            wordFrequency[word] = 1

maxFreq = 0
for word, count in wordFrequency.items():
    if count > maxFreq:
        maxFreqWord = word
        maxFreq = count

print(f"The most frequently used word with at least 6 letters is '{maxFreqWord}'")
