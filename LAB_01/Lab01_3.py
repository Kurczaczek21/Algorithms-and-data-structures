import time

name = ["M", "a", "t", "e", "u", "s", "z"]

start1=time.time()
for k in name :
    print(k)
end1=time.time()
iterowana=end1-start1

start2=time.time()
for i in range(len(name)) :
    print(name[i])
end2=time.time()
cpp=end2-start2

print("czas iterowanej petli : " + str(iterowana))
print("czas cpp petli : " + str(cpp))