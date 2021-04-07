vvod = input().split()
c = dict()
mest='0'
M = 0
sch = 2
while True:
    dot = dict()
    vvod1 = input().split()
    if len(vvod1) == 1:
        l = vvod1[0]
        break
    for i in range(len(vvod1)):
        dot[vvod[i-1]]=vvod1[i].split(',')
    c[vvod1[0]]=dot
for i in range(100000):
    if M<0:
        S=c[mest]['_']
        if S[sch-2]: l=S[sch-2]+l
    elif M>=len(l):
        S=c[mest]['_']
        if S[sch-2]: l+=S[sch-2]
    else:
        S=c[mest][l[M]]
        if S[sch-2]: l=l[:M]+S[sch-2]+l[M+1:]
    if S[sch-1] == 'L':M -= 1
    if S[sch-1] == 'R':M += 1
    if S[sch] == '!':
        print(l.replace('_',''))
        break
    if S[sch]:mest=S[sch]
