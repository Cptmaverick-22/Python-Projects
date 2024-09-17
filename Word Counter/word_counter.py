import os

file = open("test.txt", "r")
content = file.read()
words = content.split()

print(len(words))

file.close()