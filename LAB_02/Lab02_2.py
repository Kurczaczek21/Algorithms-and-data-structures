from operator import itemgetter

file = open('zadanie2.csv', 'r')

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
current_word_number=0

for i in range(len(new_file)):
    j=0
    new_file[i][1]=new_file[i][1].split(' ')
    current_word_number=len(new_file[i][1])

    while j<current_word_number:
        if len(new_file[i][1][j])>1:
            if ord(new_file[i][1][j][0])==(ord(new_file[i][1][j][1])+1) or ord(new_file[i][1][j][0])==(ord(new_file[i][1][j][1])-1):
                deleted_words.append(str(new_file[i][0])+"  "+str(new_file[i][1][j]))
                del new_file[i][1][j]
                current_word_number-=1
        j+=1

print(deleted_words)