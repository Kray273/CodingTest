students = [i for i in range(1,31)]
for x in range(28):
    attend = int(input())
    students.remove(attend) 

print(min(students))
print(max(students))