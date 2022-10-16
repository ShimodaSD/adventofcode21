with open('2021/04/giant_squid') as f:
    lines = f.read().splitlines()

def t_array(array):
    x=0
    r_array=[]
    array=list(array)
    while len(array)!=0:
        if array[0].isnumeric() and array[1].isnumeric() and len(array)>3:
            x=int(array[0])*10+int(array[1])
            array.pop(0)
            array.pop(0)
            array.pop(0)
        elif array[0].isnumeric() and array[1].isnumeric()==False :
            x=int(array[0])
            array.pop(0)
            array.pop(0)
        else:
            array.pop(0)
            array.pop(0)
        r_array.append(x)
    return r_array



board=[]
validator=lines.pop(0)
validator=list(validator)
rule=True
validator=t_array(validator)

while rule:
    for i in range(len(lines)):
        if lines[0]!='':
            xboard=lines.pop(0)
            board+=t_array(lines[0])
        else:
            lines.pop(0)   
#    for ii in range(len(validator)):    
#        for i in range(len(board)):        
#            if board[i]==validator[ii]:
               
        