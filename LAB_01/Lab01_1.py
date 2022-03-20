list = [1, 2]
suma = 3
moda = []

#for i in range (2,48):
#    if array[i-1] >= array[i-2] :
#       array.append((array[i-1]+array[i-2])/(array[i-1]-array[i-2]))
#    else:
#        array.append((array[i-1]+array[i-2])/(array[i-2]-array[i-1]))

for i in range (2,48):
       list.append((list[i-1]+list[i-2])/(list[i-1]-list[i-2]))
       suma += list[i]

for i in range(48):
       for k in range(48):
              if k!= i :       
                     if list[i]==list[k]:
                            moda.append(list[i])


srednia = suma/48
print("srednia wartosc " + str(srednia))

if len(moda)==0 :
       print("brak powtorzen")

