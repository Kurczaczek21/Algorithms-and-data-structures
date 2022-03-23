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

alreadyUsed = []

for i in range(len(new_file)):
    if int(new_file[i][0]) in alreadyUsed:
        new_file[i][0]=int(new_file[i-1][0])+1
    alreadyUsed.append(int(new_file[i][0]))

deleted_words=[]
current_file_length=len(new_file)
possition=0
while possition < current_file_length:
    new_file[possition][1]=new_file[possition][1].split(' ')
    for j in range(len(new_file[possition][1])):
        if len(new_file[possition][1][j])>1:
            if ord(new_file[possition][1][j][0])==(ord(new_file[possition][1][j][1])+1) or ord(new_file[possition][1][j][0])==(ord(new_file[possition][1][j][1])-1):
                deleted_words.append(str(new_file[possition][0])+"  "+str(new_file[possition][1][j]))
                # current_file_length-=1
                # del new_file[possition][1][j]
            possition+=1
print(deleted_words)