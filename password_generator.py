from random import randint as rand


passwd = []
while(len(passwd) < 8):
    passwd.append(str(rand(0,9)))
print("".join(passwd))