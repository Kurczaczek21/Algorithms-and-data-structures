import glob, os


# print(os.listdir('./LAB_03/zadanie1'))

files = glob.glob('LAB_03/zadanie1/*')

for line in files:
    print(type(line))
    dog=line.split('\\')[1]
    print("__________"+dog)

print(files)
