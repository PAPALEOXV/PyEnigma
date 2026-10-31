byte0=int(input())
file0=open('PyEnigma0','rb')
data0=file0.read()
file0.close()
file1=open('PyEnigma1','rb')
data1=file1.read()
file1.close()
file2=open(input(),'rb')
data2=file2.read()
file2.close()
data3=[]
for byte2 in data2:
    if byte2>125:
        byte2-=7
    elif byte2>96:
        byte2-=4
    elif byte2>64:
        byte2-=2
    elif byte2>37:
        byte2-=1
    byte2-=32
    byte2+=data0[byte0]
    while byte2>87:
        byte2-=88
    byte3=data1[byte2]
    byte0+=1
    while byte0>87:
        byte0-=88
    data3.append(byte3)
file3=open(input(),'wb')
file3.write(bytes(data3))
file3.close()