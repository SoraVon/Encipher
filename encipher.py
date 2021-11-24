# Message : Hello World
# key : test
# Encrypted Message : EXIIS  OSCIW
# f = [chr(i) for i in range(32,127)]
import math,sys

Message = input("Input the Message : ")
key = input("Input the Key : ")
EncryptedMessage = ""

AlphaBet = [chr(i) for i in range(32,127)]
Range = math.ceil(26/len(key))
#
#
Args = [[ord(i) for i in Message],[ord(i) for i in key]]
test = []
for i in key:
    if i not in test:
        test.append(i)
        index = AlphaBet.index(i)
        width = index+Range
        if width >= len(AlphaBet):
            width = width - len(AlphaBet)
        for i in range(index,width):
            if AlphaBet[i] not in test:
                test.append(AlphaBet[i])
for i in AlphaBet:
    if i not in test:
        test.append(i)

for i in Message:
    try:
        EncryptedMessage += test[AlphaBet.index(i)]
    except:
        EncryptedMessage += " "
print("Encrypted Message :",EncryptedMessage)
