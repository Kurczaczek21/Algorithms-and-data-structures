array = [1, 2]
suma = 3
moda = []

#for i in range (2,48):
#    if array[i-1] >= array[i-2] :
#       array.append((array[i-1]+array[i-2])/(array[i-1]-array[i-2]))
#    else:
#        array.append((array[i-1]+array[i-2])/(array[i-2]-array[i-1]))

for i in range (2,48):
       array.append((array[i-1]+array[i-2])/(array[i-1]-array[i-2]))
       suma += array[i]

for i in range(48):
       for k in range(48):
              if k!= i :       
                     if array[i]==array[k]:
                            moda.append(array[i])


srednia = suma/48
print("srednia wartosc " + str(srednia))

if len(moda)==0 :
       print("brak powtorzen")

