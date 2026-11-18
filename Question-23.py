
P10 = [3,5,2,7,4,10,1,9,8,6]
P8 = [6,3,7,4,8,5,10,9]
IP = [2,6,3,1,4,8,5,7]
IPI = [4,1,3,5,7,2,8,6]
EP = [4,1,2,3,2,3,4,1]
P4 = [2,4,3,1]

S0 = [[1,0,3,2],[3,2,1,0],
      [0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3],[2,0,1,3],
      [3,0,1,0],[2,1,0,3]]

def perm(b,p):
    return [b[i-1] for i in p]

def xor(a,b):
    return [x^y for x,y in zip(a,b)]

def keygen(key):
    b=perm(list(map(int,key)),P10)
    l,r=b[:5],b[5:]
    l,r=l[1:]+l[:1],r[1:]+r[:1]
    k1=perm(l+r,P8)
    l,r=l[2:]+l[:2],r[2:]+r[:2]
    k2=perm(l+r,P8)
    return k1,k2

def sbox(b,box):
    row=b[0]*2+b[3]
    col=b[1]*2+b[2]
    n=box[row][col]
    return [n//2,n%2]

def fk(b,k):
    l,r=b[:4],b[4:]
    x=xor(perm(r,EP),k)
    y=perm(sbox(x[:4],S0)+sbox(x[4:],S1),P4)
    return xor(l,y)+r

def sdes(data,key):
    k1,k2=keygen(key)
    b=perm(list(map(int,data)),IP)
    b=fk(b,k1)
    b=b[4:]+b[:4]
    b=fk(b,k2)
    return ''.join(map(str,perm(b,IPI)))

def ctr(data,key):
    result=""
    counter=0
    for i in range(0,len(data),8):
        count=format(counter,'08b')
        stream=sdes(count,key)
        block=data[i:i+8]
        result+=''.join(str(int(a)^int(b))
                        for a,b in zip(block,stream))
        counter+=1
    return result

key="0111111101"
pt="000000010000001000000100"

cipher=ctr(pt,key)
plain=ctr(cipher,key)

print("Plaintext :",pt)
print("Key       :",key)
print("Ciphertext:",cipher)
print("Decrypted :",plain)
