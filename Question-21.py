
def pad(data):
    data += b'\x80'
    while len(data) % 1 != 0:
        data += b'\x00'
    return data

def unpad(data):
    return data.rstrip(b'\x00').rstrip(b'\x80')

def encrypt(x):
    return (5 * x + 7) % 256

def decrypt(x):
    return (205 * (x - 7)) % 256

def ecb(data):
    return bytes(encrypt(x) for x in data)

def cbc(data, iv=10):
    result = []
    for x in data:
        iv = encrypt(x ^ iv)
        result.append(iv)
    return bytes(result)

def cfb(data, iv=10):
    result = []
    for x in data:
        c = x ^ encrypt(iv)
        result.append(c)
        iv = c
    return bytes(result)

text = input("Enter plaintext: ").encode()
data = pad(text)

print("Padded Text:", data)
print("ECB:", ecb(data).hex())
print("CBC:", cbc(data).hex())
print("CFB:", cfb(data).hex())
