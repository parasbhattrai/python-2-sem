name=input("Name:")
dob=input("DOB:")
reg=input("Reg no:")
dep=input("Department:")
m1=int(input("m1:"))
m2=int(input("m2:"))
m3=int(input("m3:"))
m4=int(input("m4:"))
m5=int(input("m5:"))
total=m1+m2+m3+m4+m5
per=(total/500)*100
print("Name:",name)
print("DOB:",dob)
print("Reg no:",reg)
print("Department:",dep)
print("Total:",total)
print("Percentage:",per)
if per>=50:
    print("Pass")
else:
    print("Fail")
