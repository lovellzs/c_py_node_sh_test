#coding=utf-8


res = [0,1,2,3,4,5]
print res[::-1]

res1 = set(r[1:] if r.startswith('!') else r for r in [u'csv',u'segwit']) - set(['bip65', 'csv', 'segwit'])

print res1

list1 = [1,2,3,4,5,6,6,5]
print list1

print set(list1)


print "======================="

if 'cryptonight' in ['scrypt','cryptonight']:
    print 'true'



