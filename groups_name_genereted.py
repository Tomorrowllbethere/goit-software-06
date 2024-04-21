import random 

with open("groups.txt", 'r+') as f:
    data =  f.readlines()
    new_data = []
    classes_numbers = random.randint(1, 5)
    for line in data:
        lin = line.strip()
        for i in range(1, classes_numbers):
            new_line = f'{lin}{str(i)}\n' 
            new_data.append(new_line)

with open("students_group.txt", 'w+') as f:
    for line in new_data:
        f.write(line)


print(data)
print("its fake")
print(new_data)