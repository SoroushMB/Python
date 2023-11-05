import string
sentence = "I don't know whether it will happen or not!\n"
puncs = list(string.punctuation)

for punc in puncs:
    if punc in sentence:
        sentence = sentence.replace(punc,"")
sentence = sentence.replace(" ","")
print(sentence)