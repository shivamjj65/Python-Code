# writing string given by user into list

print("Enter string values or type '\e' to exit")
l = []
i=1
ip = input("Sentence no "+str(i)+"\t") # taking first input
while(ip!='\e'):
    l.append(ip)
    i=i+1
    ip = input("Sentence no " + str(i) + "\t") # taking input till \e is typed

print("List of inputs is: ",l)

f = open("data.txt",'w')
f.writelines(l)
f.close()

f = open("data.txt",'r')
for l in f.readline():
    print(l,end=' ')
f.close()