persons = []
print(persons)

for i in range(3):
    x = input("Enter name: ")
    persons.append(x)

print(persons)

while True:
    ch = input("want to add person? enter y for yes .. other key for No")
    if ch == 'y':
        x = input('Enter name: ')
        persons.append(x)
    else:
        break

print(len(persons))
