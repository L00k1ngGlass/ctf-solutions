import base64

# enter the encoded credentials here 
smtp_b64 = ""

decoded = base64.b64decode(smtp_b64)

print(decoded.decode())
