i = int(input())

sentence = ""
for n in range(1,i+1):
    if n%2 == 1:
        sentence += "I hate"
    else:
        sentence += "I love"
    if n != i:
        sentence += " that "
sentence += " it"
print(sentence)
    
