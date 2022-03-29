import glob, os

files = glob.glob('LAB_03/zadanie1/*')

for i in range(len(files)):
    files[i]=files[i].replace('LAB_03/zadanie1\\','')
    i+=1


for i in range(len(files)):
    try:
        os.mkdir('C:\PY prog\LAB_03\zadanie1\\'+files[i][0])
    except FileExistsError:
        pass
    os.replace('C:\PY prog\LAB_03\zadanie1\\'+ files[i] , "C:\PY prog\LAB_03\zadanie1\\"+files[i][0]+ '\\'+ files[i])