f = open("abc.txt",'r')

f1 = open("write.txt",'a')

temp = 0
sum=0
list = []
for data in f:
    list.append(int(data))

print(list)

for i in range(len(list)):
    sum = sum + list[i]

f1.write(str(sum))
