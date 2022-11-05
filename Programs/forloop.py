with open("./Message.txt","w+") as file:
    for i in range(1,500):
        count = str(i)
        text = "hello, I am piyush kumar kondhol",count
        file.writelines(text)