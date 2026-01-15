student={
    "name":"shyam",
    "age":20,
    "course":"python"
}
print(student)
print(student["name"])
print(student.get("name"))
print(student.get("age"))

student["marks"]=99
print(student)
student["age"]=25
print(student)
student.update({"name":"ram"})
print(student)
student.pop("age")
print(student)
student.popitem()
print(student)

print(student.keys())

print(student.values())

for key in student:
    print(key,student.get(key))

if "name" in student:
    print("key exists")

employees={
    101:{"name":"shyam","salary":20000},
    102:{"name":"ram","salary":30000},
}
print(employees.get(101))
print(employees[101]["salary"])
