import os

file = open("Convert to txt.txt", "r")
content = file.read()
words = content.split()

print(len(words))

file.close()