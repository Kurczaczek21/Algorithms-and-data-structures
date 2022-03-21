from encodings import utf_8
import time


txt = input("Insert text: ")
word_count = len(txt.split())
txt = txt.lower()
start=time.time()

dictionary = open('SJP.txt' ,encoding='utf_8' ).read().splitlines()
if word_count==1:
    if txt in dictionary:
        print("Given word exists in polish dictionary")
    else:
        print("Given word does not exist in polish dictionary")
else:
    print("You have given "+str(word_count)+ " words.")

print(time.time()-start)