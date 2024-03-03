import hashlib

if __name__ == "__main__":
    h = hashlib.new('sha3_512')
    h.update(b"my secret password")
    hashedPass = h.hexdigest()
    h2 = hashlib.new('sha3_512')
    h2.update(b"wrong password")
    userEnteredHashedPass = h2.hexdigest()
    h3 = hashlib.new('sha3_512')
    h3.update(b"my secret password")
    correctPass = h3.hexdigest()
    print(hashedPass)
    print(userEnteredHashedPass)
    print(correctPass)
