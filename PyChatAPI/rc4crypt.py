# -*- coding: utf-8 -*-
# RC4 cryptor

class RC4Crypt(object):

    def __init__(self):
        pass

    def cipher(self, data, key):
        x = 0

        box = range(256)
        for i in range(256):
            x = (x + box[i] + ord(key[i % len(key)])) % 256
            box[i], box[x] = box[x], box[i]
    
        x = 0
        y = 0
        out = []
        
        for char in data:
            x = (x + 1) % 256
            y = (y + box[x]) % 256
            box[x], box[y] = box[y], box[x]
            out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))
    
        return ''.join(out)

if __name__=='__main__':
    print 'RC4 cryptor'
    a = raw_input('input string to encrypt:')
    rc4 = RC4Crypt()
    print '\nout string:', repr(rc4.cipher(a, b'tahci'))
    raw_input('\npress endet to exit...')
