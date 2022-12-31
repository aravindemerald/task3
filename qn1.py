#The code is a mess...Working with python for the first time
import csv

with open('onelinefile.txt','r') as textFile:
    data1 = textFile.read()

print(data1)
data = list(data1)
digits = []
words = []
decimals = []
word2=[]
a, b, c, d = 0, 0, 0, 0

str=''
for i in range(0, len(data)-1, 1):
    if data[i].isdigit() and not(data[i+1] == '.') and not(data[i-1] == '.') and not(data[i-2] == '.') and not(data[i-3] == '.'):
        digits.append(data[i])

    if data[i].isdigit() and data[i+1] == '.':
        temp = data[i] + data[i+1] + data[i+2]
        if data[i+3].isdigit():
            temp = temp + data[i+3]
            if(data[i+4].isdigit()):
                temp += data[i+4]
                i = i+5
                decimals.append(temp)
                continue
            i = i+4
            decimals.append(temp)
            continue
        decimals.append(temp)
        i = i + 3

    if data[i].isalpha():
        str=str+data[i]
    if data[i].isalpha() and (data[i+1].isdigit() or data[i+1]=='.'):
        str=str+data[i]
        words.append(str)
        str=''

for i in range(0,len(words)):  #This block is to remove a certain kind of anomalous behaviour that the code showed
    word1 = list(words[i])
    a=word1[-1]
    b=word1[0]
    word1.remove(a)
    if word1[0]==word1[1]:
        word1.remove(b)
    word2.append(word1)

k=0
str=""
arr = []
for i in range(0, 9):
    str = digits[i] + word2[k] + decimals[i]
    k += 1
    str += word2[k]
    k += 1
    a = list(str)
    arr.append(a)

with open("Filename2.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(arr)





