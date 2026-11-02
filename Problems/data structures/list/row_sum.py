lst=[
    [23,22,34],
    [67,87,87],
    [54,67,23]
]
# print(len(lst))
row=1
row_sum=0
num_rows=len(lst)
for i in range(0,len(lst)):
    for j in range(0,len(lst[i])):
        # print(lst[i][j],end=" ")
        if row == i:
            row_sum+=lst[i][j]

print(row_sum)
    