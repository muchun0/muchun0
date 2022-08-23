j = 1
while j <= 9:
    i = 1
    while i <= j:
        # if i != j:
        #     print(f'{i}*{j}={ i * j}',end=" ")
        # else:
        #     print(f'{i}*{j}={ i * j}')
        print(f'{i}*{j}={i * j}', end="\t")
        i += 1
    print()
    j += 1
'''教师版'''
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(f'{j}*{i}={i*j}', end='\t')
        j += 1
    i += 1
    print()