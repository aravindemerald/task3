import csv
with open("onelinefile") as f:
    a = f.read()
print(a)
k = 0
l = []
l1 = []
s = ''
n = ''
st = ''
i = 0
while i < len(a)-1:
    if a[i].isnumeric():
        if i < len(a):
            s += a[i]
            i += 1
            if a[i] == '.':
                s += a[i]
                i += 1

                while a[i].isnumeric():
                    s += a[i]
                    i += 1

                l1.append(s)
                s = ''
            elif a[i+1] != ".":
                l1.append(s)
                s = ''

    else:
        st=''
        while a[i].isalpha():
            st += a[i]
            i += 1
        l1.append(st)
        st = ''
    if len(l1) == 4:
        l.append(l1)
        l1=[]
print(l)

with open("filename2.csv", 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(l)
