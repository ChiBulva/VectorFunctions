import random
print(str(random.randint(1,101)))

f = open("text.txt", "w")
for num in range(1,100):
	f.write("[["+str(random.randint(1,101))+","+str(random.randint(1,101))+","+str(random.randint(1,101))+"],["+str(random.randint(1,101))+","+str(random.randint(1,101))+","+str(random.randint(1,101))+"]]\n")

f.close()