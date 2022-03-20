ciag=""
counter = 0

for i in range(500, 3001):
    if i%7==0 and i%5!=0:
        ciag+=str(i)

print(ciag)

ciag = ciag.replace("21", "XX")

for i in range(len(ciag)-1):
    if ciag[i]=="X" and ciag[i+1]=="X":
        counter+=1

print(counter)
print(ciag)