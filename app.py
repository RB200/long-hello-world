h = ['h']
e = ['e']
l = ['l']
l2 = ['l']
o = ['o']
w = ['w']
o2 = ['o']
r = ['r']
l3 = ['l']
d = ['d']

_h = ''.join(str(h[0]))
_he = ''.join([_h,str(e[0])])
_hel = ''.join([_he,str(l[0])])
_hell = ''.join([_hel,str(l2[0])])
_hello = ''.join([_hell,str(o[0])])
_hello_ = ''.join([_hello, ' '])
_hello_w = ''.join([_hello_,str(w[0])])
_hello_wo = ''.join([_hello_w,str(o2[0])])
_hello_wor = ''.join([_hello_wo,str(r[0])])
_hello_worl = ''.join([_hello_wor,str(l3[0])])
_hello_world = ''.join([_hello_worl,str(d[0])])

print(_hello_world)
