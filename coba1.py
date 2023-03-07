'''x = 0
y = 55
if x<y:
    print("yes")
if y<x:
    print("Yes")
if x:
    print("Yes")
if y:
    print("Yes")
if 'aul' in 'grault':
    print("Yes")
if 'quux' in ['foo', 'bar', 'baz']:
    print("Yes")

print('_________________________________________')

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was True')
    print('Executing statement in suite')
    print('...')
    print('Done.')
print('After conditional')

print('_________________________________________')

if 'foo' in ['bar', 'baz', 'qux']:
    print('Outer condition is True')
    if 10 > 20:
        print('Inner condition 1')
    print('Between inner conditions')
    if 10 < 20:
        print('Inner condition 2')
    print('End of outer condition')
print('After outer condition')

print('_________________________________________')

x = 120
if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

print('_________________________________________')

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000
if uang > hargaBuku:
    print('beli buku')
else:
    print('Uang tidak cukup')

print('_________________________________________')

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000
if uang > hargaBuku:
    print('beli buku')
elif uang > hargaMajalah:
    print('beli majalah')
else:
    print('Uang tidak cukup')

print('_________________________________________')

name = 'Intan'
if name == 'Amelia':
    print('Hello Amelia')
elif name == 'Putri':
    print('Hello Putri')
elif name == 'Hidayanti':
    print('Hello Hidayanti')
elif name == 'Intan':
    print('Hello Intan')
else:
    print('I dont know you are')

print('_________________________________________')

if 'a' in 'bar':
    print('Hello!')
elif 1 < 0:
    print('True')
elif var:
    print("This won't either")

print('_________________________________________')

if 'f' in 'foo': print('1');print('2');print('3')

print('_________________________________________')

x=2
if x == 1: print('foo');print('bar')
elif x == 2: print('qux');print('quux')
else: print('corge');print('grault')

print('_________________________________________')

x=2
if x == 1:
    print('foo')
    print('bar')
elif x == 2:
    print('qux')
    print('quux')
else: 
    print('corge')
    print('grault')

print('_________________________________________')

raining = False
print("Let's go to the", 'beach' if not raining else 'library' )

print('_________________________________________')

if True:
    pass
print('foo')'''

x = 0
while (x < 100):
    x+=2
print(x)

for l in 'Idaz':
    if l == 'a':
        pass
    print(l, end=", ")