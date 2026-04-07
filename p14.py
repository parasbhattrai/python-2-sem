name=input("Enter name:")
yob=int(input("Enter year of birth:"))
age=2026-yob
print("Name:",name)
if age>=60:
    print("Senior citizen")
else:
    print("Not a senior citizen")