import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

class LFSR:
    def __init__(self, key, taps):
        d = max(taps)
        self._s = key
        self._t = [d - t for t in taps]

    def _sum(self, L):
        s = 0
        for x in L:
            s ^= x
        return s

    def _clock(self):
        b = self._s[0]
        self._s = self._s[1:] + [self._sum(self._s[p] for p in self._t)]
        return b

    def bit(self):
        return self._clock()


class Jeff:
    def __init__(self, key):
        key = [int(i) for i in list("{:069b}".format(key))]
        self.LFSR = [
            LFSR(key[:19], [19, 18, 17, 14]),
            LFSR(key[19:46], [27, 26, 25, 22]),
            LFSR(key[46:], [23, 22, 20, 18]),
        ]

    def bit(self):
        b = [lfsr.bit() for lfsr in self.LFSR]
        return b[1] if b[0] else b[2]


def decrypt_flag(key, iv, ciphertext):
    sha1 = hashlib.sha1()
    sha1.update(str(key).encode('ascii'))
    aes_key = sha1.digest()[:16]
    cipher = AES.new(aes_key, AES.MODE_CBC, bytes.fromhex(iv))
    decrypted_flag = unpad(cipher.decrypt(bytes.fromhex(ciphertext)), 16)
    return decrypted_flag.decode()

# Brute force LFSR1 (19-bit)
def brute_force_lfsr1(output):
    for key1 in range(2**19):
        lfsr1 = LFSR([int(i) for i in list(f"{key1:019b}")], [19, 18, 17, 14])
        stream = [lfsr1.bit() for _ in range(len(output))]
        if stream == output:
            return key1
    return None

# Brute force LFSR2 (27-bit) và LFSR3 (23-bit)
def brute_force_lfsr23(lfsr1_bits, lfsr2_output, lfsr3_output):
    for key2 in range(2**27):
        lfsr2 = LFSR([int(i) for i in list(f"{key2:027b}")], [27, 26, 25, 22])
        for key3 in range(2**23):
            lfsr3 = LFSR([int(i) for i in list(f"{key3:023b}")], [23, 22, 20, 18])
            
            stream2 = [lfsr2.bit() for _ in range(len(lfsr2_output))]
            stream3 = [lfsr3.bit() for _ in range(len(lfsr3_output))]
            
            # Kết hợp theo bit điều khiển của LFSR1
            combined_stream = [stream2[i] if lfsr1_bits[i] else stream3[i] for i in range(len(lfsr1_bits))]
            
            if combined_stream == lfsr2_output:  # Kiểm tra nếu stream khớp
                return key2, key3
    return None, None


stream_output = [1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1]

# AES encryption details từ output của chương trình
iv = '310c55961f7e45891022668eea77f805'
ciphertext = '2aa92761b36a4aad9a578d6cd7a62c52ba0709cb560c0ecff33a09e4af43bff0a1c865023bf28b387df91d6319f0e103d39dda88a88c14cfcec94c8ad02a6fb3152a4466c1a184f69184349e576d8950cac0a5b58bf30e67e5269883596a33a6'

# Brute force LFSR1 để lấy bit điều khiển
# Brute force LFSR1 để lấy bit điều khiển
lfsr1_bits = stream_output  # Sử dụng trực tiếp stream_output làm bit đầu ra của LFSR1
key1 = brute_force_lfsr1(lfsr1_bits)
if key1 is not None:
    print(f"LFSR1 key found: {key1}")
    
    # Tiếp tục brute force LFSR2 và LFSR3
    lfsr2_output = stream_output  # Sử dụng stream_output làm đầu ra cho LFSR2
    lfsr3_output = stream_output  # Sử dụng stream_output làm đầu ra cho LFSR3
    key2, key3 = brute_force_lfsr23(lfsr1_bits, lfsr2_output, lfsr3_output)
    
    if key2 is not None and key3 is not None:
        print(f"LFSR2 key found: {key2}")
        print(f"LFSR3 key found: {key3}")
        
        # Ghép các key lại để tạo key 69-bit
        full_key = (key1 << (27 + 23)) | (key2 << 23) | key3
        
        # Giải mã flag
        flag = decrypt_flag(full_key, iv, ciphertext)
        print(f"Flag: {flag}")

