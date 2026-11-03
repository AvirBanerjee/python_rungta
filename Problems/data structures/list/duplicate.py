def remove_duplicate(lst)->list:
    # new_lst=set(lst) -> first solution
    # empty_lst=[]
    # for val in lst:
    #     if val not in empty_lst:
    #         empty_lst.append(val)
    # return empty_lst
    # return list(empty_lst)
    
    # print("lenght inside function",len(lst))
    empty_lst=[]
    k=0
    for i in range(0,len(lst)):
        if lst.count(lst[i])==1:
            k+=1
        if lst[i] in empty_lst:
            continue
        else:
            empty_lst.append(lst[i])
    return empty_lst,k    


lst=[8,6,7,8,7,6,5,4,5,6,4,3,2]
lst.sort()
# print(lst)
# print("lenght",len(lst))

# print(type(remove_duplicate(lst)))
print(remove_duplicate(lst))