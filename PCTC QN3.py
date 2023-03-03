input1 = int(input())
input2 = int(input())
input3 = int(input())

sidelength = min(input1,input2,input3)
if input2 == 4*sidelength:
    perimeter = input2
    area = input3
else:
    perimeter = input3
    area =  input2

print(sidelength +'\n'+ perimeter +'\n'+ area)
