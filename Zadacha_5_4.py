read = 'read.txt'
write = 'write.txt'
data = open(read,'r')

for line in data:
    newtext = line

with open (write, 'w') as data2:
    count = 1
    for i in range(len(newtext)-1):
        if i <= len(newtext):
            if newtext[i] == newtext[i + 1]:
                count += 1
            else:
                a = newtext[i]
                data2.writelines(str(count))
                data2.writelines(newtext[i])
                count = 1
    data2.writelines(str(count))
    data2.writelines(newtext[i])
