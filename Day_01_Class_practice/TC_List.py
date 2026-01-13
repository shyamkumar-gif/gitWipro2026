numbers=[10,20,30,40,50]

names=["ram","krishna","john"]
mixed=[1,"python",3.5,True]
numbers[1]=100
print(numbers)
print(names)
print(mixed)

for i in numbers:
    print(i)

if 10 in numbers:
    print("Found")

matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)

names.reverse()
print(names)

names.append("shyam")
print(names)

names.extend("travis")
print(names)

names.remove("shyam")
print(names)

names.insert(4,"shyam")
print(names)




