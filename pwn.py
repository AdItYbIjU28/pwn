from pwn import *
import math

C= remote('challenges.traboda.com',30840)
C.recvuntil('>')
C.sendline('madrid')
print(C.recvline())
C.recvuntil('>')
C.sendline('vincent van gogh')
print(C.recvline())
C.recvuntil('>')
C.sendline('alan turing')
print(C.recvline())

C.recvuntil('mean!\n\n\t')
s=[]
l=[]

for i in range(5):
        r=C.recvline()
        for j in r.split():
                s.append(j)
for m in s:
        if m.isdigit():
               l.append(int(m))
A = sum(l)/len(l)
average=math.floor(A)
C.sendline(str(average))
print(C.recvline())
a=C.recvline()
for i in a.split():
        if i.isdigit():
               b=i
C.sendline(str(A*int(b)))
print(C.recvline())

C.recvuntil('order!\n')

r=C.recvline()
list=[]
for i in r.split():
        if i.isdigit():
               list.append(int(i))
list.sort()
for i in list:
       C.send(str(i))
       C.send(' ')
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())
print(C.recvline())

c.recvuntil('t?\n\n')
c.sendline(b' crypto{ASCII_pr1nt4bl3}')
print(C.recvline())
