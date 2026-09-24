# marks={
#     1:[0,2,1],
#     "webdev":2,
#     "python":0,
#     "group":{
#         "leetcode":200,
#         "hakerrank":150
#     }
# }
# print(marks)

student={
    "name":"Avir",
    "roolNo":34,
    "Subjects":["pyhton","azure","webdev"],
    "Topics":["CSS","Dict","App Service"],
    "Address":{
        1:"Ghana",
        2:"kahamaria",
        3:"Jabalpur"
    },
    "isGooodPerson":False,
    "CGPA":9.8
}
# student["PassOutYear"]=2020
# student["isGooodPerson"]=True
# print(student.get("Semester"))
# print("After error")
# top=student.get("Topics")
# top.pop(0)
# print(student)
# student.pop("isGooodPerson")
# print(student)
# removed_item=student.popitem()
# print(removed_item)
# del student["isGooodPerson"]
# print(student)
# print(student.keys())
# print(student.values())
# print(student.items())

# for key in student:
#     print(key)

for key,value in student.items():
    print(key,value)