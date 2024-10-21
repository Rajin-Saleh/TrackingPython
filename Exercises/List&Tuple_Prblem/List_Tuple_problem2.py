#  Write a program to accept marks of 6 students and display them in a sorted manner.

mark = []

st1 = int(input("Enter your marks :"))
mark.append(st1)
st2 = int(input("Enter your marks :"))
mark.append(st2)
st3 = int(input("Enter your marks :"))
mark.append(st3)
st4 = int(input("Enter your marks :"))
mark.append(st4)
st5 = int(input("Enter your marks :"))
mark.append(st5)
st6 = int(input("Enter your marks :"))
mark.append(st6)

mark.sort()
print(mark)
