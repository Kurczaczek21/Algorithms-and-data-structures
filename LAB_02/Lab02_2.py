file = open('C:\PY prog\LAB_02\zadanie2.csv', 'r')

new_file = []
for row in file:
    id=row.split(',', 1)[0]
    value= row.split(',', 1)[1].replace('\n','').lower()
    if value != '' and value != 'val':
        new_row=id +", "+value
        new_file.append(new_row)

def take_id(x):
    return new_file[int(x)].split(', ', 1)[0]

new_file.sort(key=take_id)

for i in range(10):
    print(new_file[i])

