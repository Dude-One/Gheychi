BASE62_CHARS = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encode_base62(num: int):
    if num < 0:
        raise ValueError("Number must be non-negative")

    if num == 0:
        return BASE62_CHARS[0]

    base62 = []
    while num > 0:
        num, rem = divmod(num, 62)
        base62.append(BASE62_CHARS[rem])

    return "".join(reversed(base62))


def decode_base62(base62_str: str):
    num = 0
    for char in base62_str:
        value = BASE62_CHARS.index(char)
        num = num * 62 + value
    return num
