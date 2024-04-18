a = [1,2,3,4,5,-1,-4,-6]
text = open("Ab1/text.txt", "r")
text_w = text.read()
txet = open("Ab1/txet.txt", "w")
word_count = dict()

for i in a:
    if i > 0:
        print (i, end=" ")
print()

#print(text_w)
words = text_w.split()
for i in words:
    if i in word_count:
        word_count[i] += 1
    else:
        word_count[i] = 1

print(word_count)

abc = text_w[::-1]
print(abc)
txet.write(abc)

text.close()
txet.close()

#2.4 Missing