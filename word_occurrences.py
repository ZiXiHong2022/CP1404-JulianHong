dic_sentence = {}
count = 1
sentence = str(input("Text:")).split()
for i in sentence:
    if i == sentence:
        count += 1
        dic_sentence[i] = count
    else:
        count = 1
        dic_sentence[i] = count
d = dic_sentence
for a in d:
    print(f"{a}\t : {d[a]}")







