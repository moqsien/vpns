import base64

def decode_base64(content:str)->bytes:
    length = len(content)
    count = 4-(length%4)
    if count > 0 and count < 4:
        content += "="*count
    bstr = base64.b64decode(content)
    return bstr
