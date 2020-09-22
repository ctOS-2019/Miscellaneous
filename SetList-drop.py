lst = eval(input('请输入列表lst:'))
lst2 = list(set(lst))
lst3 = []
for i in range(len(lst2)):
    apper = 0
    for y in range(len(lst)):
        if lst2[i] == lst[y]:
            apper += 1
    if apper == 1:
        lst3.append(lst2[i])
print(lst3)
