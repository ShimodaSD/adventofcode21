with open('binary_diag') as f:
    lines = f.read().splitlines()
x=0
gamma=0
epsilon=0
power=0
validator=[]
o2=[]


def validar(arrayx):
    for a in arrayx:
        o=str("".join(filter(str.isdigit, a)))
        o=list(o)
        for y in range(len(o)):
            if o[y] == '0':
                validator[-len(o)+y]+=-1
            elif o[y]== '1':
                validator[-len(o)+y]+=1
    for a in range(len(validator)):
        if validator[a]>0:
            validator[a]=1
        elif validator[a]==0:
            validator[a]=1
        else:
            validator[a]=0

for i in range(len(str("".join(filter(str.isdigit, lines[0]))))):
    validator.append(0)
xvalidator=validator.copy()
validar(lines)
for a in range(len(validator)):
    x+=validator[len(validator)-a-1]*10**a
gamma=int(str(x),2)
epsilon = 2** len(validator) + ~gamma
power=gamma*epsilon
print(power)


co2=lines.copy()
o2=co2.copy()

for a in range(12):
    d=0
    x=0
    validator=xvalidator.copy()
    validar(co2)
    while d< len(co2):
        valid=co2[d]
        valid=[int(item) for item in valid]
        if valid[a]==validator[a] and len(co2)!=1:
            co2.remove(co2[d])
            x=1
        #elif valid[a]==0 and len(co2)!=1 and len(co2)%2==0 and x==0:
        #    co2.remove(co2[d])
        else:
            d+=1

for a in range(12):
    d=0
    x=0
    validator=xvalidator.copy()
    validar(o2)
    while d< len(o2):
        valid=o2[d]
        valid=[int(item) for item in valid]
        if valid[a]!=validator[a] and len(o2)!=1:
            o2.remove(o2[d])
            x=1   
        elif valid[a]!=1 and len(o2)!=1 and len(o2)%2==0 and x==0:
            o2.remove(o2[d])
        else:
            d+=1

gamma=int(o2[0],2)
epsilon=int(co2[0],2)
print(gamma*epsilon)