import base64
import base64

# Base64����
base64_str = 'Tk5ZV00zQkFKUkVFUUxLSUxGRlMyTVJRR0kyQ0E9PT0='
base64_decoded = base64.b64decode(base64_str).decode('utf-8')
print('Base64������:', base64_decoded)

# Base32����
base32_str = base64_decoded
base32_decoded = base64.b32decode(base32_str).decode('utf-8')
print('Base32������:', base32_decoded)