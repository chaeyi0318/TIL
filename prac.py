# for i in range(2):
#     print(f'{i}층')
#     for j in range(0, 4):
#         print(f'{j}호')

# for hour in range(1, 13):
#     for min in range(1, 61):
#         print(f'{hour}')

elements = [['A', 'B'], ['c', 'd']]


# for i in range(len(elements)):
#     print(elements[i][0])

#     if i == 1:
#         for j in range(0, 2):
#             print(elements[j][1])
#     else:
#         continue

# for i in range(len(elements[0])):
#     print(elements[0][i])

#     for j in range(len(elements[1])):
#         print(elements[1][j])

for i in elements[0]:
    print(i)

    for j in elements[1]:
        print(j)