import hashlib

def HashGen(long_url):
    UrlHash = hashlib.sha256(str(long_url).encode("utf-8")).hexdigest()
    return UrlHash


