list_1=[10,32,22,67,21, 54,87 ]
for i in range(len(list_1)-1):
    for j in range(len(list_1)-1):
     if list_1[j]>list_1[j+1]:
      list_1[j],list_1[j+1]=list_1[j+1],list_1[j]
print(list_1)