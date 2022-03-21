import time


txt = input("Dowolny teks: ")

word_count = len(txt.split())
print(word_count)

txt = txt.lower()

print(txt)

start=time.time()

print(time.time()-start)