BASE62_ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base62_encode(num):
    result = ""
    if num == 0:
        return BASE62_ALPHABET[0]
    while num > 0:
        num, remainder = divmod(num, 62)
        result = BASE62_ALPHABET[remainder] + result
    return result
