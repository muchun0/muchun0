list = [30,27,2,67,99,5]
# for i in range(len(list)):
#     for j in range(len(list)):
#         if list[i] < list[j]:
#             list[i],list[j] = list[j],list[i]
# else:
#     print(list)

for i in range(len(list)-1):
    for j in range(len(list) -1 -i):
        if list[j] > list[j+1]:
            list[j],list[j+1] = list[j+1],list[j]
else:
    print(list)

