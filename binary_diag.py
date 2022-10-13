from sre_constants import RANGE_UNI_IGNORE


with open('binary_diag.txt') as f:
    lines = f.readlines()
x=0
gamma=0
epsilon=0
power=0
c=[]
for i in range(len(str("".join(filter(str.isdigit, lines[0]))))):
    c.append(0)

for a in lines:
    o=str("".join(filter(str.isdigit, a)))
    o=list(o)
    for y in range(len(o)):
        if o[y] == '0':
            c[-len(o)+y]+=-1
        elif o[y]== '1':
            c[-len(o)+y]+=1
            

for a in range(len(c)):
    if c[a]>0:
        c[a]=1
    else:
        c[a]=0
for a in range(len(c)):
    x+=c[a]*10**a
gamma=int(str(x),2)
epsilon = int(''.join('0' if c=='1' else ('1' if c=='0' else c) for c in str(x)),2)
power=gamma*epsilon
print(power)