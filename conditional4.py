age = int(input("enter age:"))

if age > 18:
    print("This person is an adult.")
elif age >= 13 and age <= 18:
    print("This person is a teen.")
else:
    print("This person is a child.")