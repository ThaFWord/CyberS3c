#!/usr/bin/python3

file = open("resultado1.txt", "w")

print("For loop" "\n")
file.write("For loop" '\n')

x = ["windows", "macos", "linux", "solaris", "android", "ios"] 
for i in x:
    if i != "solaris":
        print(i)
        file.write(str(i) + '\n')


print("\n")
file.write("\n")
    
print("While loop" "\n" )
file.write('\n' + "While loop" + '\n')

idx = 0
while idx < len(x):
    if x[idx] != "solaris":
        print(x[idx])
        file.write(str(x[idx]) + '\n')
    idx += 1
   
file.close()
