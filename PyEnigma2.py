byte0=0
byte1=int(input())
file1=open('PyEnigma3','rb')
data1=list(file1.read())
file1.close()
byte2=int(input())
file2=open('PyEnigma1','rb')
data2=list(file2.read())
file2.close()
file3=open(input(),'rb')
data3=list(file3.read())
file3.close()
for byte3 in data3:
    if byte3>96:
        byte3-=4
    elif byte3>64:
        byte3-=2
    elif byte3>35:
        byte3-=1
    byte3-=32
    byte3=data1[byte3]
    if byte3>96:
        byte3-=4
    elif byte3>64:
        byte3-=2
    elif byte3>35:
        byte3-=1
    byte3-=byte1
    while byte3<32:
        byte3+=87
    byte1+=1
    while byte1>86:
        byte1-=87
    byte3-=32
    byte3=data2[byte3]
    if byte3>96:
        byte3-=4
    elif byte3>64:
        byte3-=2
    elif byte3>35:
        byte3-=1
    byte3-=byte2
    while byte3<32:
        byte3+=87
    byte2+=1
    while byte2>86:
        byte2-=87
    if byte3>92:
        byte3+=4
    elif byte3>62:
        byte3+=2
    elif byte3>34:
        byte3+=1
    data3[byte0]=byte3
    byte0+=1
file3=open(input(),'wb')
file3.write(bytes(data3))
file3.close()