alphabet='abcdefghijklmnopqrstuvwxyz'
def encrypt(sentence,num):
    words=sentence.split()
    newWords=[]
    for word in words:
        newWord=''
        for i in word:
            number=(alphabet.index(i)+num) %26
            newWord+=(alphabet[number])
        newWords.append(newWord)
    return " ".join(newWords)

def decrypt(encrypted,key):
    return encrypt(encrypted,-key)

def hack(encrypted):
    pass

if __name__ == "__main__":
    print(encrypt('i am happy',3))
    print(decrypt('l dp kdssb',3))

