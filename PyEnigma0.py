byte0=32
file1=open(input(),'rb')
data1=file1.read()
file1.close()
data2=[0]*87
for byte1 in data1:
    if byte1>96:
        byte1-=4
    elif byte1>64:
        byte1-=2
    elif byte1>35:
        byte1-=1
    byte1-=32
    byte2=byte0
    if byte2>92:
        byte2+=4
    elif byte2>62:
        byte2+=2
    elif byte2>34:
        byte2+=1
    data2[byte1]=byte2
    byte0+=1
    while byte0>118:
        byte0-=87
file2=open(input(),'wb')
file2.write(bytes(data2))
file2.close()