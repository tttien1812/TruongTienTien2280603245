from Crypto.Hash import SHA3_256

def sha3(message):
    """Hàm tính toán giá trị băm SHA3-256."""
    sha3_hash = SHA3_256.new() 
    sha3_hash.update(message)  
    return sha3_hash.digest()  

def main():
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    
    hashed_text = sha3(text)
    
    print("Chuỗi văn bản đã nhập: {}".format(text.decode('utf-8')))
    print("SHA3-256 Hash: {}".format(hashed_text.hex()))

if __name__ == "__main__":
    main()
