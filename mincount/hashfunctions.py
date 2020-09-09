from typing import Callable
import hashlib
import zlib


def __common(n: int, h: Callable, digest_size: int, b=0) -> float:
    assert b <= digest_size
    if b == 0:
        return int.from_bytes(h(n.to_bytes(8, "big")).digest(), 'big') / 2**digest_size
    else:
        return (int.from_bytes(h(n.to_bytes(8, "big")).digest(), 'big')  >> (digest_size - b)) / 2**b


def md5(n: int, b=0) -> float:
    return __common(n, hashlib.md5, 128, b)


def sha1(n: int, b=0) -> float:
    return __common(n, hashlib.sha1, 160, b)


def sha12(n: int) -> int:
    return int(hashlib.sha1(n.to_bytes(8, "big")).hexdigest()[:8], 16)


def sha224(n: int, b=0) -> float:
    return __common(n, hashlib.sha224, 224, b)


def sha256(n: int, b=0) -> float:
    return __common(n, hashlib.sha256, 256, b)


def sha384(n: int, b=0) -> float:
    return __common(n, hashlib.sha384, 384, b)


def sha512(n: int, b=0) -> float:
    return __common(n, hashlib.sha512, 512, b)


def blake2b(n: int, b=0) -> float:
    return __common(n, hashlib.blake2b, 512, b)


def blake2s(n: int, b=0) -> float:
    return __common(n, hashlib.blake2s, 256, b) #pylint: disable=no-member


def blake2s2(n: int) -> int:
    return int(hashlib.blake2s(n.to_bytes(8, "big")).hexdigest()[:8], 16) #pylint: disable=no-member


def sha3_224(n: int, b=0) -> float:
    return __common(n, hashlib.sha3_224, 224, b)


def sha3_256(n: int, b=0) -> float:
    return __common(n, hashlib.sha3_256, 256, b)


def sha3_384(n: int, b=0) -> float:
    return __common(n, hashlib.sha3_384, 384, b)


def sha3_512(n: int, b=0) -> float:
    return __common(n, hashlib.sha3_512, 512, b)


def adler32(n: int, b=0) -> float:
    if b == 0:
        return zlib.adler32(n.to_bytes(8, "big")) / 2**32
    else:
        return (zlib.adler32(n.to_bytes(8, "big")) >> (32 - b)) / 2**b


def adler322(n: int) -> int:
    return zlib.adler32(n.to_bytes(8, "big"))


def crc32(n: int, b=0) -> float:
    if b == 0:
        return zlib.crc32(n.to_bytes(8, "big")) / 2**32
    else:
        return (zlib.crc32(n.to_bytes(8, "big")) >> (32 - b)) / 2**b


def crc322(n: int) -> int:
    return zlib.crc32(n.to_bytes(8, "big"))


hash_functions = {
    "md5": md5,
    "sha1": sha1,
    "sha224": sha224,
    "sha256": sha256,
    "sha384": sha384,
    "sha512": sha512,
    "blake2b": blake2b,
    "blake2s": blake2s,
    "sha3_224": sha3_224,
    "sha3_256": sha3_256,
    "sha3_384": sha3_384,
    "sha3_512": sha3_512,
    "adler32": adler32,
    "crc32": crc32
}


def main():
    for name, h in hash_functions.items():
        a = [h(n, 16) for n in range(10000)]
        print(name)
        print(min(a))
        print(max(a))


if __name__ == "__main__":
    main()
