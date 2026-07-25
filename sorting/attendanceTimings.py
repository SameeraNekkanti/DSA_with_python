n=int(input("enter the no. of students: "))

students=[]

print("enter roll no. and entry time: ")
for i in range(n):
    roll=input("enter roll no.")
    time=input("entry time: ")
    students.append([roll, time])

for i in range (n-1):
    swapped=False

    for j in range (n-i-1):
        if students[j][1]>students[j+1][1]:
            students[j], students[j+1]=students[j+1], students[j]
            swapped=True

    if not swapped:
        break


print("\nStudents sorted by entry time:")
for s in students:
    print("roll no: ", s[0],"entry time: ", s[1])

