name = "Pen Sakahbotra"
age = 20
major = "Data Science"
gpa = 3.69
is_scholar = False

print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Major   : {major}")
print(f"GPA     : {gpa:.2f}")
print(f"Scholar : {is_scholar}")

for value in (name, age, major, gpa, is_scholar):
    print(repr(value), "->", type(value).__name__)
