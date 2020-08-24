#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib, binascii

def pbkdf2sha1hex(x, salt, iters):
    h = hashlib.pbkdf2_hmac('sha1', x, salt, iters)
    return binascii.hexlify(h)

def pbkdf2sha256hex(x, salt, iters):
    h = hashlib.pbkdf2_hmac('sha256', x, salt, iters)
    return binascii.hexlify(h)

print('C1b3rwall Academy 2020')
print('======================')
print('PBKDF-HMAC-SHA1:')
h1 = pbkdf2sha1hex(b'https://www.ecteg.eu/c1b3rwall-academy-es/there-are-no-flags-here/', b'c1b3rwall', 1000000)
h2 = pbkdf2sha1hex(b')(H?\x8b\xaa\xe6Zh\xfe\x12\xdf`66\x15\xe5\xa7?\xc1', b'c1b3rwall', 1000000) 
print(h1)
print(h2)
print('PBKDF-HMAC-SHA256:')
h1 = pbkdf2sha256hex(b'https://www.ecteg.eu/c1b3rwall-academy-es/there-are-no-flags-here/', b'c1b3rwall', 1000000)
h2 = pbkdf2sha256hex(b'\xce\xa9\xe6fIFM\xb5\xc7n\xde\xdb4o9b\x85\xfa\xf0\xb6&9\x97\xc5]\xfb\x12c\xad\xfe\x97u', b'c1b3rwall', 1000000)
print(h1)
print(h2)
print('PBKDF-HMAC-SHA1:')
h1 = pbkdf2sha1hex(b'https://www.ecteg.eu/c1b3rwall-academy-es/calculate-the-correct-flag/', b'c1b3rwall', 1000000)
h2 = pbkdf2sha1hex(b'\xd4\x8f\x02\xc7wJ\xa2\x8f\\\xdc\xfe\xd2\xf6 \xd2\xab\x06S\x1e}', b'c1b3rwall', 1000000)
print(h1)
print(h2)
print('PBKDF-HMAC-SHA256:')
h1 = pbkdf2sha256hex(b'https://www.ecteg.eu/c1b3rwall-academy-es/calculate-the-correct-flag/', b'c1b3rwall', 1000000)
h2 = pbkdf2sha256hex(b'????????', b'c1b3rwall', 1000000)
print(h1)
print(b'--->' + h2 + b'<---')
print("------- FLAG: -------")
print("Your goal is calculate the value that collides the message. Please input it module3{b'value'}")
