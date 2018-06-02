#coding=utf-8

import struct

def ser_string(s):
    if len(s) < 253:
        return chr(len(s)) + s
    elif len(s) < 0x10000:
        return chr(253) + struct.pack("<H", len(s)) + s
    elif len(s) < 0x100000000L:
        return chr(254) + struct.pack("<I", len(s)) + s
    return chr(255) + struct.pack("<Q", len(s)) + s

def deser_uint256(f):
    r = 0L
    for i in xrange(8):
        t = struct.unpack("<I", f.read(4))[0]
        r += t << (i * 32)
    return r

#====
def ser_uint256(u):
    rs = ""
    for i in xrange(8):
        rs += struct.pack("<I", u & 0xFFFFFFFFL)
        u >>= 32
    return rs

def uint256_from_str(s):
    r = 0L
    t = struct.unpack("<IIIIIIII", s[:32])

    for i in xrange(8):
        print "%x"%t[i]
        r += t[i] << (i * 32)
    return r

#d81c41b9419f120ab07a280a9818871aceafff59ebb70b14615875f79d1b1886
if __name__ == '__main__':
    hashstr ="d81c41b9419f120ab07a280a9818871aceafff59ebb70b14615875f79d1b1886" ##64*4=256位 = 32 * 8
    # print len(hashstr)

    hash = 0xd81c41b9419f120ab07a280a9818871aceafff59ebb70b14615875f79d1b1886
    aa= "%x"%hash
    # print aa
    print "",ser_uint256(hash)

    print "%x"%uint256_from_str( ser_uint256(hash) )

    # print "%x"%int(hashstr,16)
