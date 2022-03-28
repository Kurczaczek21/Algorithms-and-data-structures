import glob, os


# print(os.listdir('./LAB_03/zadanie1'))

files = glob.glob('LAB_03/zadanie1/*')

for i in range(len(files)):
    files[i]=files[i].replace('LAB_03/zadanie1\\','')
    i+=1
# for i in range(26):
#     new_folder=(chr(65+i))
#     os.mkdir(os.path.join('E:\PROGRAMMS\Collage-AiSD\LAB_03\SORTED FOLDERS',new_folder ))

sorted=glob.glob('LAB_03/SORTED FOLDERS/*')

for i in range(len(sorted)):
    sorted[i]=sorted[i].replace('LAB_03/SORTED FOLDERS\\','')
    i+=1

for j in range(len(files)):
    for i in range(len(sorted)):
        if sorted[i]==files[j][0]:
            source=files[j]
            dest=sorted[i]
            os.replace('E:\PROGRAMMS\Collage-AiSD\LAB_03\zadanie1\\'+ source , "E:\PROGRAMMS\Collage-AiSD\LAB_03\SORTED FOLDERS\\"+dest)
    