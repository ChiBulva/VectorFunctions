import random
print(str(random.randint(1,101)))

f = open("text.txt", "w")
for num in range(1,1000):
    if(num==999):
        f.write(str(random.randint(1,100))+","+str(random.randint(1,100))+","+str(random.randint(1,100))+"|"+str(random.randint(1,100))+","+str(random.randint(1,100))+","+str(random.randint(1,100)))
        #print("HI")
        #f.write(str(num)+","+str(num)+","+str(num)+"|"+str(num)+","+str(num)+","+str(num))
    else:
        f.write(str(random.randint(1,100))+","+str(random.randint(1,100))+","+str(random.randint(1,100))+"|"+str(random.randint(1,100))+","+str(random.randint(1,100))+","+str(random.randint(1,100))+"\n")
        #f.write(str(num)+","+str(num)+","+str(num)+"|"+str(num)+","+str(num)+","+str(num)+"\n")
	
	
f.close()