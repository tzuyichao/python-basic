# aes_gcm_compat.py
import os
from base64 import b64decode, b64encode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

_ENV_NAMES = ("KEY", "AES_KEY")

def _load_key() -> bytes:
    for name in _ENV_NAMES:
        b64 = os.getenv(name)
        if b64:
            key = b64decode(b64)
            if len(key) in (16, 24, 32):
                return key
            raise RuntimeError("AES key must be 16/24/32 bytes after Base64 decoding.")
    raise RuntimeError('Missing env var: set "KEY" (or "AES_KEY") to Base64(raw_key).')

def encrypt_for_java(plaintext: str) -> str:
    """
    回傳 Base64( IV(12) || CIPHERTEXT || TAG(16) )
    與 Java AES/GCM/NoPadding（GCMParameterSpec(128, iv)）相容。
    """
    key = _load_key()
    iv = os.urandom(12)  # GCM 推薦 12-byte nonce
    encryptor = Cipher(algorithms.AES(key), modes.GCM(iv)).encryptor()
    ct = encryptor.update(plaintext.encode("utf-8")) + encryptor.finalize()
    tag = encryptor.tag  # 16 bytes
    blob = iv + ct + tag
    return b64encode(blob).decode("ascii")

def decrypt_from_java(b64_ciphertext: str) -> str:
    """
    解 Base64( IV(12) || CIPHERTEXT || TAG(16) )
    """
    key = _load_key()
    blob = b64decode(b64_ciphertext)
    if len(blob) < 12 + 16:
        raise ValueError("cipher blob too short")
    iv = blob[:12]
    tag = blob[-16:]
    ct  = blob[12:-16]

    decryptor = Cipher(algorithms.AES(key), modes.GCM(iv, tag)).decryptor()
    plain = decryptor.update(ct) + decryptor.finalize()
    return plain.decode("utf-8")

if __name__ == "__main__":
    # 自我測試：Python 加 → Python 解
    b64 = encrypt_for_java("hello GCM")
    print("PY->B64:", b64)
    print("PY->PY:", decrypt_from_java(b64))
