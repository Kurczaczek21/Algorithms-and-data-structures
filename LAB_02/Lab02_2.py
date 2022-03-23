from operator import itemgetter

file = open('E:\PROGRAMMS\Collage-AiSD\LAB_02\zadanie2.csv', 'r')

new_file = []

for row in file:
    id=row.split(',', 1)[0]
    value= row.split(',', 1)[1].replace('\n','').lower()
    if value != '' and value != 'val':
        new_row =[]
        new_row.append(str(id) +", "+str(value))
        new_file.append(new_row)

new_file = [sub.split(', ',1) for subl in new_file for sub in subl]


new_file=sorted(new_file, key=itemgetter(0))

for i in range(10):
    print(new_file[i][0])

