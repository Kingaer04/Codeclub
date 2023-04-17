with open("C:\\Users\\DanAnny\\Documents\\Python\\data\\testing.txt", "r") as file:
    word = file.read().split(" ")
    print(dict((i, word.count(i)) for i in set(word)))
