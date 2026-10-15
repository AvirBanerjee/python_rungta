import copy
# org=[1,2,3,4,5,6,7]
# print("org before->",org)
# cpy=org
# cpy.append(100)
# print("org->",org)
# print("cpy->",cpy)

# shallow copy
# org=[1,2,3,4,5,6,7]
# print("org before->",org)
# cpy=copy.copy(org)
# cpy.append(100)
# print("org->",org)
# print("cpy->",cpy)


# deep copy
org=[1,2,3,[4,5],[6,7]]
print("org before->",org)
cpy=copy.deepcopy(org)
cpy[3].append("vir")
print("org->",org)
print("cpy->",cpy)